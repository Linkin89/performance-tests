from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum

from clients.http.gateway.cards.schema import CardSchema


class AccountType(StrEnum):
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"

    def __repr__(self) -> str:
        return self.value


class AccountStatus(StrEnum):
    ACTIVE = "ACTIVE"
    PENDING_CLOSURE = "PENDING_CLOSURE"
    CLOSED = "CLOSED"

    def __repr__(self) -> str:
        return self.value


class AccountSchema(BaseModel):
    """Структура данных аккаунта"""
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsResponseSchema(BaseModel):
    """Структура ответа получения счёта"""
    accounts: list[AccountSchema]


class GetAccountsQuerySchema(BaseModel):
    """
    Структура данных для получения списка счетов пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(serialization_alias="userId")


class OpenDepositAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия депозитного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(serialization_alias="userId")


class OpenDepositAccountResponseSchema(BaseModel):
    """
    Структура данных ответа открытия депозитного счета.
    """
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия сберегательного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(serialization_alias="userId")


class OpenSavingsAccountResponseSchema(BaseModel):
    """
    Структура данных ответа открытия сберегательного счета.
    """
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """
    Структура данных для открытия дебетового счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(serialization_alias="userId")


class OpenDebitCardAccountResponseSchema(BaseModel):
    """
    Структура данных ответа открытия дебетового счета.
    """
    account: AccountSchema


class OpenCreditCardAccountRequestSchema(BaseModel):
    """
    Структура данных для запроса открытия счёта кредитной карты.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(serialization_alias="userId")


class OpenCreditCardAccountResponseSchema(BaseModel):
    """
    Структура данных ответа открытия счёта кредитной карты.
    """
    account: AccountSchema
