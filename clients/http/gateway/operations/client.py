from typing import Literal, TypedDict

from httpx import QueryParams, Response
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class BaseOperationBodyDict(TypedDict):
    """Базовая структура данных для создания операций."""
    status: Literal['FAILED', 'COMPLETED', 'IN_PROGRESS', 'UNSPECIFIED']
    amount: int
    cardId: str
    accountId: str


class GetOperationIdPathDict(TypedDict):
    """Структура данных для получения информацци об операции."""
    operation_id: str


class GetOperationReceiptPathDict(TypedDict):
    """Структура данных для получения чека по операции."""
    operation_id: str


class GetOperationsQueryDict(TypedDict):
    """Структура данных для получения списка операций для определенного счета."""
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """Структура данных для получения статистики по операциям для определенного счета."""
    accountId: str


class MakeFeeOperationBodyDict(BaseOperationBodyDict):
    """Структура данных для создания операции комиссии."""
    ...


class MakeTopUpOperationBodyDict(BaseOperationBodyDict):
    """Структура данных для создания операции пополнения."""
    ...


class MakeCashbackOperationBodyDict(BaseOperationBodyDict):
    """Структура данных для создания операции кэшбэка."""
    ...


class MakeTransferOperationBodyDict(BaseOperationBodyDict):
    """Структура данных для создания операции перевода."""
    ...


class MakePurchaseOperationBodyDict(BaseOperationBodyDict):
    """Структура данных для создания операции покупки."""
    category: str


class MakeBillPaymentOperationBodyDict(BaseOperationBodyDict):
    """Структура данных для создания операции оплаты по счету."""
    ...


class MakeCashWithdrawalOpertionBodyDict(BaseOperationBodyDict):
    """Структура данных для создания операции снятия наличных денег."""
    ...


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия c /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: GetOperationIdPathDict) -> Response:
        """
        Получение информации об операции по `operation_id`.

        :param operation_id: id операции
        :returns Response: объект httpx.Response
        """
        return self.get(url=f'/api/v1/operations/{operation_id}')

    def get_operation_receipt_api(self, operation_id: GetOperationReceiptPathDict) -> Response:
        """
        Получение чека по операции по `operation_id`.

        :param operation_id: id операции
        :returns Response: объект httpx.Response
        """
        return self.get(url=f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.

        :param accountId: id аккаунта
        :returns Response: объект httpx.Response
        """
        return self.get(url='/api/v1/operations/operations/', params=query(QueryParams(**query)))

    def get_opertions_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param accountId: id аккаунта
        :returns Response: объект httpx.Response
        """
        return self.get(url='/api/v1/operations/operations-summary', params=query(QueryParams(**query)))

    def make_fee_operation_api(self, body: MakeFeeOperationBodyDict) -> Response:
        """
        Создание операции комиссии.

        :param body: данные для создания операции комиссии
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-fee-operation', json=body)

    def make_top_up_operation_api(self, body: MakeTopUpOperationBodyDict) -> Response:
        """
        Создание операции пополнения.
        :param body: данные для создания операции пополнения
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-top-up-operation', json=body)

    def make_cashback_operation_api(self, body: MakeCashbackOperationBodyDict) -> Response:
        """
        Создание операции кэшбэка.

        :param body: данные для создания операции кэшбэка
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-cashback-operation', json=body)

    def make_transfer_operation_api(self, body: MakeTransferOperationBodyDict) -> Response:
        """
        Создание операции перевода.

        :param body: данные для создания операции перевода
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-transfer-operation', json=body)

    def make_purchase_operation_api(self, body: MakePurchaseOperationBodyDict) -> Response:
        """
        Создание операции покупки.

        :param body: данные для создания операции покупки
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-purchase-operation', json=body)

    def make_bill_payment_operation_api(self, body: MakeBillPaymentOperationBodyDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param body: данные для создания операции оплаты по счёту
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-bill-payment-operation', json=body)

    def make_cash_withdrawal_operation_api(self, body: MakeCashWithdrawalOpertionBodyDict) -> Response:
        """
        Создание операции снятия наличных денег.

        :param body: данные для создания операции оплаты по счёту
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-cash-withdrawal-operation', json=body)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(build_gateway_http_client())
