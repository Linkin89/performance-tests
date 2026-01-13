from pydantic import BaseModel, EmailStr, ConfigDict, Field


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

    email: EmailStr
    last_name: str = Field(serialization_alias="lastName")  # пришлось использовать serialization,
    first_name: str = Field(serialization_alias="firstName")  # т.к. при alias ругается валидатор Pylance в VSCode
    middle_name: str = Field(serialization_alias="middleName")
    phone_number: str = Field(serialization_alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа `создания` пользователя.
    """
    user: UserSchema
