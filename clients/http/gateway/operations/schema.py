from datetime import datetime
from enum import StrEnum
from pydantic import BaseModel, Field, ConfigDict, UUID4, HttpUrl
from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

    def __repr__(self) -> str:
        return self.value


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

    def __repr__(self) -> str:
        return self.value


class OperationSchema(BaseModel):
    """Структура данных по операции"""
    model_config = ConfigDict(populate_by_name=True)

    id: UUID4
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: UUID4 = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: UUID4 = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """Структура данных чека"""
    url: HttpUrl
    document: str


class OperationsSummarySchema(BaseModel):
    """Структура данных общей сводки по операциям"""
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class MakeFeeOperationResponseSchema(BaseModel):
    """Структура данных ответа создания операции списания комиссии"""
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """Структура данных ответа создания операции пополнения"""
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """Структура данных ответа создания операции кэшбэка"""
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """Структура данных ответа создания операции перевода"""
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """Структура данных ответа создания операции покупки"""
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Структура данных ответа создания операции оплаты по счёту"""
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Структура данных ответа создания операции обналичивания"""
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """Структура данных ответа получения чека"""
    receipt: OperationReceiptSchema


class MakeOperationRequestSchema(BaseModel):
    """Базовая структура данных для создания операций."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(serialization_alias="cardId")
    account_id: str = Field(serialization_alias="accountId")


class GetOperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema


class GetOperationResponseSchema(BaseModel):
    operation: OperationSchema


class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]


class GetOperationsQuerySchema(BaseModel):
    """Структура данных для получения списка операций для определенного счета."""
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(serialization_alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """Структура данных для получения статистики по операциям для определенного счета."""
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(serialization_alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции комиссии."""
    ...


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции пополнения."""
    ...


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции кэшбэка."""
    ...


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции перевода."""
    ...


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции покупки."""
    category: str = Field(default_factory=fake.category)


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции оплаты по счету."""
    ...


class MakeCashWithdrawalOpertionRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции снятия наличных денег."""
    ...
