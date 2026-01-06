from typing import Literal, TypedDict
from httpx import Response
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CardDict(TypedDict):
    """Структура карты"""
    id: str
    pin: str
    cvv: str
    type: Literal["UNSPECIFIED", "VIRTUAL", "PHYSICAL"]
    status: Literal["UNSPECIFIED", "ACTIVE", "FROZEN", "CLOSED", "BLOCKED"]
    account: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: Literal["UNSPECIFIED", "MASTERCARD", "VISA"]


class IssueVirtualCardResponseDict(object):
    """Структура ответа созданной виртуальной карты"""
    card: CardDict


class IssuePhysicalCardResponseDict(object):
    """Структура ответа созданной физической карты"""
    card: CardDict


class IssueVirtualCardRequestDict(TypedDict):
    """Структура данных для запроса создания виртуальной карты"""
    userId: str
    accountId: str


class IssuePhysicalCardRequestDict(TypedDict):
    """Структура данных для запроса создания физической карты"""
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, json: IssueVirtualCardRequestDict) -> Response:
        """
        Создать виртуальную карту для пользователя по его userId и accountId.

        :param json: json содержащий userId и accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/cards/issue-virtual-card', json=json)

    def issue_physical_card_api(self, json: IssuePhysicalCardRequestDict) -> Response:
        """
        Создать физическую карту для пользователя по его userId и accountId.

        :param json: json содержащий userId и accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/cards/issue-physical-card', json=json)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseDict:
        request = IssueVirtualCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_virtual_card_api(request)
        return response.json()

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseDict:
        request = IssuePhysicalCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_physical_card_api(request)
        return response.json()


def build_cards_http_gateway_client() -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
