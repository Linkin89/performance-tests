from typing import TypedDict
from httpx import Response
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class IssueVirtualCardDict(TypedDict):
    """Структура данных для создания виртуальной карты"""
    userId: str
    accountId: str


class IssuePhysicalCardDict(TypedDict):
    """Структура данных для создания физической карты"""
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, json: IssueVirtualCardDict) -> Response:
        """
        Создать виртуальную карту для пользователя по его userId и accountId.

        :param json: json содержащий userId и accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/cards/issue-virtual-card', json=json)

    def issue_physical_card_api(self, json: IssuePhysicalCardDict) -> Response:
        """
        Создать физическую карту для пользователя по его userId и accountId.

        :param json: json содержащий userId и accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/cards/issue-physical-card', json=json)


def build_cards_http_gateway_client() -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
