import joblib
import numpy as np
import pandas as pd
import sklearn.ensemble


if __name__ == '__main__':
    print('Training Model')

    url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    df = pd.read_csv(url)
    include = ['Age', 'Sex', 'Embarked', 'Survived']  # Only four features
    df = df[include]

    categoricals = []
    for col, col_type in df.dtypes.iteritems():
        if col_type == 'O':
            categoricals.append(col)
        else:
            df[col].fillna(0, inplace=True)

    df = pd.get_dummies(df, columns=categoricals, dummy_na=True)

    x = df[df.columns.difference(['Survived'])]
    y = df['Survived']

    rf = sklearn.ensemble.RandomForestClassifier()
    rf = rf.fit(x, y)

    print('Saving Model')
    joblib.dump(rf, 'models/model.pkl')

    print('Saving Features')
    model_columns = list(x.columns)
    joblib.dump(model_columns, 'models/model_columns.pkl')

    print('Done!')
