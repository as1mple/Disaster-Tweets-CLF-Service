import sys
import pickle

from fastapi.responses import JSONResponse
from fastapi import APIRouter
from loguru import logger

from src.modules.data_models import ResponseModel, Message, RequestParams
from src.modules import processing

logger.configure(
    handlers=[
        {"sink": sys.stderr, "level": "DEBUG"},
        dict(
            sink="logs/debug.log",
            format="{time} {level} {message}",
            level="DEBUG",
            rotation="1 weeks",
        ),
    ]
)
router = APIRouter()
logger.info("FASTAPI RUN")
router.model = pickle.load(open("resources/model.pkl", "rb"))

DEFAULT_RESPONSES = {500: {"model": Message}}


@router.get("/api/v1/status", response_model=Message, responses={**DEFAULT_RESPONSES})
def get_satus():
    logger.info("Health check")
    return Message(message="Success")


@router.post("/api/v1/text/", response_model=ResponseModel)
async def predict(text: RequestParams):
    logger.info("Run predict")
    try:
        text = str(text)
        x_test = processing.piepline_preprocess([text])
        result = router.model.predict(x_test)
        predict_proba = max(router.model.predict_proba(x_test)[0])

        return ResponseModel(predict=result, probability=predict_proba)
    except AttributeError:
        mes = "wrong format"
        logger.exception(mes)
        return JSONResponse(status_code=500, content={"message": mes})
