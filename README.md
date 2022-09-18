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

- - -
## DVC base-command

``` bash
dvc init
```

``` bash
dvc remote add -d storage gdrive://YOUR_FOLDER-NAME
```

``` bash
dvc add resources/data.txt
```

``` bash
dvc run -n split \
    -p split \
    -d resources/data.txt \
    -d requirements.txt \
    -d src/split.py \
    -o resources/train.txt \
    -o resources/test.txt \
    python src/split.py
```

``` bash
dvc run -n split -p split -d resources/data.txt -d requirements.txt -d src/split.py -o resources/train.txt -o resources/test.txt python src/split.py
```

``` bash
dvc run -n train \
    -p train \
    -d resources/train.txt \
    -d requirements.txt \
    -d src/train.py \
    -o resources/model.txt \
    python src/train.py
```

``` bash
dvc run -n train -p train -d resources/train.txt -d requirements.txt -d src/train.py -o resources/model.txt python src/train.py
```

``` bash
dvc run -n eval \
    -p eval \
    -d resources/test.txt \
    -d resources/model.txt \
    -d requirements.txt \
    -d src/eval.py \
    -M metrics.yaml \
    python src/eval.py
```

``` bash
dvc run -n eval -p eval -d resources/test.txt -d resources/model.txt -d requirements.txt -d src/eval.py -M metrics.yaml python src/eval.py
```

``` bash
dvc dag  # Visualize a DVC Pipeline
