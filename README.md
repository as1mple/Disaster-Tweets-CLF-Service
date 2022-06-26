 # DisasterTweets

## DVC

> pip install -r requirements_dvc.txt
>
> dvc pull
>
> dvc repro

## FastAPI

### Run FastApi
> pip install -r requirements.txt
> 
> uvicorn src.start_api:app


### Build & Run docker with fastapi
> dvc pull; dvc repro && sudo docker build -t fastapi_tweets -f Dockerfile .
>
> sudo docker run -p 8080:5011 -v /{full path to project}/logs/:/app/logs/ fastapi_tweets

### Update to actual model & Run docker with fastapi

>dvc pull resources/model.pkl && sudo docker run -p 8080:5011 -v /{full path to project}/logs/:/app/logs/ fastapi_tweets

## Build & Run Train docker
> sudo docker build -t repro -f Dockerfile.repro . && sudo docker run -v /{full path to project}/:/app/  repro