from time import time
from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class UserDict(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponseDict(TypedDict):
    """
    Описание структуры ответа `получения` пользователя.
    """
    user: UserDict


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры `запроса создания` пользователя.
    """
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа `создания` пользователя.
    """
    user: UserDict


class UsersGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway.
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, body: CreateUserRequestDict) -> Response:
        """
        Создание нового пользователя.

        :param body: Словарь с данными нового пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/users", json=body)

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id).json()
        return response

    def create_user(self) -> CreateUserResponseDict:
        name = f"vadim{time()}"
        new_user = CreateUserRequestDict(
            email=f"{name}@example.com",
            lastName="string",
            firstName="string",
            middleName="string",
            phoneNumber="string"
        )
        return self.create_user_api(new_user).json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
