from pydantic import BaseModel


class Message(BaseModel):
    message: str


class RequestParams(BaseModel):
    text: str


class ResponseModel(BaseModel):
    predict: int
    probability: float
