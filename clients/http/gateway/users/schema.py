from xml.sax import default_parser_list
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from pytest import File
from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа `получения` пользователя.
    """
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры `запроса создания` пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(serialization_alias="lastName", default_factory=fake.last_name)  # пришлось использовать serialization,
    first_name: str = Field(serialization_alias="firstName", default_factory=fake.first_name)  # т.к. при alias ругается валидатор Pylance в VSCode
    middle_name: str = Field(serialization_alias="middleName", default_factory=fake.middle_name)
    phone_number: str = Field(serialization_alias="phoneNumber", default_factory=fake.phone_number)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа `создания` пользователя.
    """
    user: UserSchema
