from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    new_user = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(new_user)
    return new_user
