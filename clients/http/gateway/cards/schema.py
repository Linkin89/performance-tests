from enum import StrEnum
from pydantic import BaseModel, ConfigDict, Field


class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"

    def __repr__(self) -> str:
        return self.value


class CardStatus(StrEnum):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"

    def __repr__(self) -> str:
        return self.value


class CardPaymentSystem(StrEnum):
    MASTERCARD = "MASTERCARD"
    VISA = "VISA"

    def __repr__(self) -> str:
        return self.value


class CardSchema(BaseModel):
    """Структура карты"""
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: CardPaymentSystem = Field(alias="paymentSystem")


class IssueVirtualCardResponseSchema(BaseModel):
    """Структура ответа созданной виртуальной карты"""
    card: CardSchema


class IssuePhysicalCardResponseSchema(BaseModel):
    """Структура ответа созданной физической карты"""
    card: CardSchema


class IssueVirtualCardRequestSchema(BaseModel):
    """Структура данных для запроса создания виртуальной карты"""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(serialization_alias="userId")
    account_id: str = Field(serialization_alias="accountId")


class IssuePhysicalCardRequestSchema(BaseModel):
    """Структура данных для запроса создания физической карты"""
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(serialization_alias="userId")
    account_id: str = Field(serialization_alias="accountId")
