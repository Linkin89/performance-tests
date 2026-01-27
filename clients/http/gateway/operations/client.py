from httpx import QueryParams, Response
from locust.env import Environment
from pydantic import UUID4
from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import (build_gateway_http_client,
                                         build_gateway_locust_http_client)
from clients.http.gateway.operations.schema import (
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationsSummaryResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeCashWithdrawalOperationResponseSchema,
    MakeCashWithdrawalOpertionRequestSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия c /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: UUID4) -> Response:
        """
        Получение информации об операции по `operation_id`.

        :param operation_id: id операции
        :returns Response: объект httpx.Response
        """
        return self.get(url=f'/api/v1/operations/{operation_id}',
                        extensions=HTTPClientExtensions(route="/api/v1/operations/{operation_id}"))

    def get_operation_receipt_api(self, operation_id: UUID4) -> Response:
        """
        Получение чека по операции по `operation_id`.

        :param operation_id: id операции
        :returns Response: объект httpx.Response
        """
        return self.get(url=f'/api/v1/operations/operation-receipt/{operation_id}',
                        extensions=HTTPClientExtensions(route="/api/v1/operations/operation-receipt/{operation_id}"))

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение списка операций для определенного счета.

        :param accountId: id аккаунта
        :returns Response: объект httpx.Response
        """
        return self.get(url='/api/v1/operations/',
                        params=QueryParams(**query.model_dump(by_alias=True)),
                        extensions=HTTPClientExtensions(route="/api/v1/operations/{operation_id}"))

    def get_opertions_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param accountId: id аккаунта
        :returns Response: объект httpx.Response
        """
        return self.get(url='/api/v1/operations/operations-summary',
                        params=QueryParams(**query.model_dump(by_alias=True)),
                        extensions=HTTPClientExtensions(route="/api/v1/operations/operations-summary/{operation_id}"))

    def make_fee_operation_api(self, json: MakeFeeOperationRequestSchema) -> Response:
        """
        Создание операции комиссии.

        :param body: данные для создания операции комиссии
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-fee-operation', json=json.model_dump(by_alias=True))

    def make_top_up_operation_api(self, json: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создание операции пополнения.
        :param body: данные для создания операции пополнения
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-top-up-operation', json=json.model_dump(by_alias=True))

    def make_cashback_operation_api(self, json: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создание операции кэшбэка.

        :param body: данные для создания операции кэшбэка
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-cashback-operation', json=json.model_dump(by_alias=True))

    def make_transfer_operation_api(self, json: MakeTransferOperationRequestSchema) -> Response:
        """
        Создание операции перевода.

        :param body: данные для создания операции перевода
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-transfer-operation', json=json.model_dump(by_alias=True))

    def make_purchase_operation_api(self, json: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создание операции покупки.

        :param body: данные для создания операции покупки
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-purchase-operation', json=json.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, json: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Создание операции оплаты по счету.

        :param body: данные для создания операции оплаты по счёту
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-bill-payment-operation', json=json.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, json: MakeCashWithdrawalOpertionRequestSchema) -> Response:
        """
        Создание операции снятия наличных денег.

        :param body: данные для создания операции оплаты по счёту
        :returns Request: объект httpx.Response
        """
        return self.post(url='/api/v1/operations/make-cash-withdrawal-operation', json=json.model_dump(by_alias=True))

    def get_operation(self, operation_id: UUID4) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: UUID4) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_opertions_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        json = MakeFeeOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_fee_operation_api(json=json)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        json = MakeTopUpOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_top_up_operation_api(json=json)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        json = MakeCashbackOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cashback_operation_api(json=json)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self,
                                card_id: str,
                                account_id: str) -> MakeTransferOperationResponseSchema:
        json = MakeTransferOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_transfer_operation_api(json=json)
        return response.json()

    def make_purchase_operation(self, card_id: str,
                                account_id: str, category: str) -> MakePurchaseOperationResponseSchema:
        json = MakePurchaseOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_purchase_operation_api(json=json)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        json = MakeBillPaymentOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_bill_payment_operation_api(json=json)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self,
                                       card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        json = MakeCashWithdrawalOpertionRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cash_withdrawal_operation_api(json=json)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(build_gateway_http_client())


def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayHTTPClient с хуками сбора метрик.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))
