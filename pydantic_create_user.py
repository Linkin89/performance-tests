from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """Структура данных пользователя"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class CreateUserRequestSchema(BaseModel):
    """Структура данных для создания пользователя"""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class CreateUserResponseSchema(BaseModel):
    """Структура данных ответа создания пользователя """
    user: UserSchema
