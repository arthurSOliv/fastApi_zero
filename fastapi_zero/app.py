from http import HTTPStatus
from fastapi import FastAPI

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=Message
)
def read_root():
    # return 123 this will return erro because it does not match the response model
    return {'message': 'Hello World!'}
