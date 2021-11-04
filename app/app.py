import fastapi
import joblib
import os
import pandas as pd
import pydantic
import uvicorn


path = os.path.abspath('models')
rf = joblib.load(os.path.join(path, 'model.pkl'))
model_columns = joblib.load(os.path.join(path, 'model_columns.pkl'))

app = fastapi.FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello, stranger'}


class Item(pydantic.BaseModel):
    Age: float
    Sex: str
    Embarked: str

# Expose the prediction functionality, make a prediction from the passed
# JSON data and return the prediction
@app.post('/predict')
def predict(item: Item):
    data = item.dict()
    df = pd.DataFrame(data, index=[0])
    categoricals = ['Sex', 'Embarked']
    df['Age'].fillna(0, inplace=True)

    df = pd.get_dummies(df, columns=categoricals, dummy_na=True)
    df = df.reindex(columns=model_columns, fill_value=0)

    prediction = int(rf.predict(df))

    return {'prediction': prediction}


# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
