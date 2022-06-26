FROM python:3.8
ARG DEBIAN_FRONTEND=noninteractive

COPY requirements.txt ./requirements.txt
COPY requirements_dvc.txt ./requirements_dvc.txt

RUN python -m pip install -U pip && \
    python -m pip install -r requirements.txt && \
    python -m pip install -r requirements_dvc.txt && \
    python -m pip cache purge \

COPY ./ /app/

WORKDIR /app/

CMD dvc pull && uvicorn src.api_run:app --host=0.0.0.0 --port=${PORT:-5011}
