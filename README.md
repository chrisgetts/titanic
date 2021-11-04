This repo serves as a POC for (1) packaging a ML model into an API and (2) containerizing the API with Docker  
  
1. train the model by running train.py. This will train a simple random forest model to predict whether a person will survive the titanic. The output of this script will be  
  (1) model.pkl - the random forest classifier  
  (2) model_columns.pkl - the columns used in the random forest classifier.  
These two outputs will be saved to a folder called "models/".  
  CMD: `python train.py`  
  ![Alt text](img/train.PNG?raw=true "Training")

2. build the docker image. In the same directory as Dockerfile run the following  
  CMD: `docker build -t titanic . `  
  ![Alt text](img/docker_build.PNG?raw=true "Building")

3. deploy the docker container.  
  CMD: `docker build -t -i -p 8000:8000 titanic`
  ![Alt text](img/docker_run.PNG?raw=true "Deploying")

4. navigate to `localhost:8000`. You should see the following message.
  *{"message":"Hello, stranger"}*
  
5. test out the api via swagger docs by navigating to `localhost:8000/docs`  
The api requires only 3 fields: Age (int), Sex (str: "male" or "female"), and Embarked (str: "S", "C", "Q").  
The api should return a prediction either 1 or 0.  

![Alt text](img/aoi_request.PNG?raw=true "Request")
![Alt text](img/aoi_response.PNG?raw=true "Response")

**Example**  
Request body *{  
  "Age": 22,    
  "Sex": "female",  
  "Embarked": "Q"  
}*  
  
200 Response *{     
  "prediction": 1  
}*  
