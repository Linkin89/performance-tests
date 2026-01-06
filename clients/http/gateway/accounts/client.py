from typing import Literal, TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.cards.client import CardDict
from clients.http.gateway.client import build_gateway_http_client


class AccountDict(TypedDict):
    """Структура данных аккаунта"""
    id: str
    type: Literal["UNSPECIFIED", "DEBIT_CARD", "CREDIT_CARD", "DEPOSIT", "SAVINGS"]
    cards: list[CardDict]
    status: Literal["UNSPECIFIED", "ACTIVE", "PENDING_CLOSURE", "CLOSED"]
    balance: float


class GetAccountsResponseDict(TypedDict):
    """Структура ответа получения счёта"""
    accounts: list[AccountDict]


class GetAccountsQueryDict(TypedDict):
    """
    Структура данных для получения списка счетов пользователя.
    """
    userId: str


class OpenDepositAccountRequestDict(TypedDict):
    """
    Структура данных для открытия депозитного счета.
    """
    userId: str


class OpenDepositAccountResponseDict(TypedDict):
    """
    Структура данных ответа открытия депозитного счета.
    """
    account: AccountDict


class OpenSavingsAccountRequestDict(TypedDict):
    """
    Структура данных для открытия сберегательного счета.
    """
    userId: str


class OpenSavingsAccountResponseDict(TypedDict):
    """
    Структура данных ответа открытия сберегательного счета.
    """
    account: AccountDict


class OpenDebitCardAccountRequestDict(TypedDict):
    """
    Структура данных для открытия дебетового счета.
    """
    userId: str


class OpenDebitCardAccountResponseDict(TypedDict):
    """
    Структура данных ответа открытия дебетового счета.
    """
    account: AccountDict


class OpenCreditCardAccountRequestDict(TypedDict):
    """
    Структура данных для запроса открытия счёта кредитной карты.
    """
    userId: str


class OpenCreditCardAccountResponseDict(TypedDict):
    """
    Структура данных ответа открытия счёта кредитной карты.
    """
    account: AccountDict


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway.
    """

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка счетов пользователя.

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get("/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, body: OpenDepositAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия депозитного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=body)

    def open_savings_account_api(self, body: OpenSavingsAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия сберегательного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-savings-account", json=body)

    def open_debit_card_account_api(self, body: OpenDebitCardAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия дебетовой карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-debit-card-account", json=body)

    def open_credit_card_account_api(self, body: OpenCreditCardAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-credit-card-account", json=body)

    def get_accounts(self, user_id: str) -> GetAccountsResponseDict:
        query = GetAccountsQueryDict(userId=user_id)
        response = self.get_accounts_api(query)
        return response.json()

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseDict:
        request = OpenDepositAccountRequestDict(userId=user_id)
        response = self.open_deposit_account_api(request)
        return response.json()

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseDict:
        request = OpenSavingsAccountRequestDict(userId=user_id)
        response = self.open_savings_account_api(request)
        return response.json()

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseDict:
        request = OpenDebitCardAccountRequestDict(userId=user_id)
        response = self.open_debit_card_account_api(request)
        return response.json()

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseDict:
        request = OpenCreditCardAccountRequestDict(userId=user_id)
        response = self.open_credit_card_account_api(request)
        return response.json()


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Функция создаёт экземпляр AccountsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AccountsGatewayHTTPClient.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())
