from clients.http.gateway.cards.schema import (IssuePhysicalCardRequestSchema,
                                               IssuePhysicalCardResponseSchema,
                                               IssueVirtualCardRequestSchema,
                                               IssueVirtualCardResponseSchema)
from httpx import Response
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, json: IssueVirtualCardRequestSchema) -> Response:
        """
        Создать виртуальную карту для пользователя по его userId и accountId.

        :param json: json содержащий userId и accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/cards/issue-virtual-card', json=json.model_dump(by_alias=True))

    def issue_physical_card_api(self, json: IssuePhysicalCardRequestSchema) -> Response:
        """
        Создать физическую карту для пользователя по его userId и accountId.

        :param json: json содержащий userId и accountId
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url='/api/v1/cards/issue-physical-card', json=json.model_dump(by_alias=True))

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        request = IssueVirtualCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request)
        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        request = IssuePhysicalCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)


def build_cards_http_gateway_client() -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())

