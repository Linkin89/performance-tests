from typing import Literal, TypedDict

from httpx import QueryParams, Response
from clients.http.client import HTTPClient


class BaseOperationResponseDict(TypedDict):
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


class MakeFeeOperationResponseDict(BaseOperationResponseDict):
    """Структура данных для создания операции комиссии."""
    ...


class MakeTopUpOperationResponseDict(BaseOperationResponseDict):
    """Структура данных для создания операции пополнения."""
    ...


class MakeCashbackOperationResponseDict(BaseOperationResponseDict):
    """Структура данных для создания операции кэшбэка."""
    ...


class MakeTransferOperationResponseDict(BaseOperationResponseDict):
    """Структура данных для создания операции перевода."""
    ...


class MakePurchaseOperationResponseDict(BaseOperationResponseDict):
    """Структура данных для создания операции покупки."""
    category: str


class MakeBillPaymentOperationResponseDict(BaseOperationResponseDict):
    """Структура данных для создания операции оплаты по счету."""
    ...


class MakeCashWithdrawalOpertionResponseDict(BaseOperationResponseDict):
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

    def make_fee_operation_api(self, body: MakeFeeOperationResponseDict) -> Response:
        """
        Создание операции комиссии.

        :param body: данные для создания операции комиссии
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-fee-operation', json=body)

    def make_top_up_operation_api(self, body: MakeTopUpOperationResponseDict) -> Response:
        """
        Создание операции пополнения.
        :param body: данные для создания операции пополнения
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-top-up-operation', json=body)

    def make_cashback_operation_api(self, body: MakeCashbackOperationResponseDict) -> Response:
        """
        Создание операции кэшбэка.

        :param body: данные для создания операции кэшбэка
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-cashback-operation', json=body)

    def make_transfer_operation_api(self, body: MakeTransferOperationResponseDict) -> Response:
        """
        Создание операции перевода.

        :param body: данные для создания операции перевода
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-transfer-operation', json=body)

    def make_purchase_operation_api(self, body: MakePurchaseOperationResponseDict) -> Response:
        """
        Создание операции покупки.

        :param body: данные для создания операции покупки
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-purchase-operation', json=body)

    def make_bill_payment_operation_api(self, body: MakeBillPaymentOperationResponseDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param body: данные для создания операции оплаты по счёту
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-bill-payment-operation', json=body)

    def make_cash_withdrawal_operation_api(self, body: MakeCashWithdrawalOpertionResponseDict) -> Response:
        """
        Создание операции снятия наличных денег.

        :param body: данные для создания операции оплаты по счёту
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-cash-withdrawal-operation', json=body)
