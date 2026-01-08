from datetime import datetime
from typing import Literal, TypedDict

from httpx import QueryParams, Response
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """Структура данных по операции"""
    id: str
    type: Literal["FEE", "TOP_UP", "PURCHASE", "CASHBACK", "TRANSFER", "BILL_PAYMENT", "CASH_WITHDRAWAL"]
    status: Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]
    amount: float
    cardId: str
    category: str
    createdAt: datetime
    accountId: str


class OperationReceiptDict(TypedDict):
    """Структура данных чека"""
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """Структура данных общей сводки по операциям"""
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class MakeFeeOperationResponseDict(TypedDict):
    """Структура данных ответа создания операции списания комиссии"""
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    """Структура данных ответа создания операции пополнения"""
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """Структура данных ответа создания операции кэшбэка"""
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """Структура данных ответа создания операции перевода"""
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """Структура данных ответа создания операции покупки"""
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """Структура данных ответа создания операции оплаты по счёту"""
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """Структура данных ответа создания операции обналичивания"""
    operation: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    """Структура данных ответа получения чека"""
    receipt: OperationReceiptDict


class MakeOperationRequestDict(TypedDict):
    """Базовая структура данных для создания операций."""
    status: Literal['FAILED', 'COMPLETED', 'IN_PROGRESS', 'UNSPECIFIED']
    amount: float
    cardId: str
    accountId: str


class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict


class GetOperationResponseDict(TypedDict):
    operation: OperationDict


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]


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


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции комиссии."""
    ...


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции пополнения."""
    ...


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции кэшбэка."""
    ...


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции перевода."""
    ...


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции покупки."""
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции оплаты по счету."""
    ...


class MakeCashWithdrawalOpertionRequestDict(MakeOperationRequestDict):
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

    def make_fee_operation_api(self, body: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        :param body: данные для создания операции комиссии
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-fee-operation', json=body)

    def make_top_up_operation_api(self, body: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения.
        :param body: данные для создания операции пополнения
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-top-up-operation', json=body)

    def make_cashback_operation_api(self, body: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка.

        :param body: данные для создания операции кэшбэка
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-cashback-operation', json=body)

    def make_transfer_operation_api(self, body: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода.

        :param body: данные для создания операции перевода
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-transfer-operation', json=body)

    def make_purchase_operation_api(self, body: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.

        :param body: данные для создания операции покупки
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-purchase-operation', json=body)

    def make_bill_payment_operation_api(self, body: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param body: данные для создания операции оплаты по счёту
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-bill-payment-operation', json=body)

    def make_cash_withdrawal_operation_api(self, body: MakeCashWithdrawalOpertionRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.

        :param body: данные для создания операции оплаты по счёту
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-cash-withdrawal-operation', json=body)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        path = GetOperationIdPathDict(operation_id=operation_id)
        response = self.get_operation_api(path)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        path = GetOperationReceiptPathDict(operation_id=operation_id)
        response = self.get_operation_receipt_api(path)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id) -> GetOperationsSummaryResponseDict:
        query = GetOperationsQueryDict(account_id)
        response = self.get_opertions_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        body = MakeFeeOperationRequestDict(status="COMPLETED",
                                           amount=55.77,
                                           cardId=card_id,
                                           accountId=account_id)
        response = self.make_fee_operation_api(body=body)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        body = MakeTopUpOperationRequestDict(status="FAILED",
                                             amount=12.32,
                                             cardId=card_id,
                                             accountId=account_id)
        response = self.make_top_up_operation_api(body=body)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        body = MakeCashbackOperationRequestDict(status="IN_PROGRESS",
                                                amount=4.5,
                                                cardId=card_id,
                                                accountId=account_id)
        response = self.make_cashback_operation_api(body=body)
        return response.json()

    def make_transfer_operation(self,
                                card_id: str,
                                account_id: str) -> MakeTransferOperationResponseDict:
        body = MakeTransferOperationRequestDict(status="UNSPECIFIED",
                                                amount=234.0,
                                                cardId=card_id,
                                                accountId=account_id)
        response = self.make_cashback_operation_api(body=body)
        return response.json()

    def make_purchase_operation(self, card_id: str,
                                account_id: str, category: str) -> MakePurchaseOperationResponseDict:
        body = MakePurchaseOperationRequestDict(status="COMPLETED",
                                                amount=342.32,
                                                cardId=card_id,
                                                accountId=account_id,
                                                category=category)
        response = self.make_purchase_operation_api(body=body)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        body = MakeBillPaymentOperationRequestDict(status="COMPLETED",
                                                   amount=2.3,
                                                   cardId=card_id,
                                                   accountId=account_id)
        response = self.make_bill_payment_operation_api(body=body)
        return response.json()

    def make_cash_withdrawal_operation(self,
                                       card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        body = MakeCashWithdrawalOpertionRequestDict(status="FAILED",
                                                     amount=34234.45,
                                                     cardId=card_id,
                                                     accountId=account_id)
        response = self.make_bill_payment_operation_api(body=body)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(build_gateway_http_client())
