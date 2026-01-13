from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """Описание структуры документа"""
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """Структура данных ответа получения тарифа """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """Структура данных ответа получения контракта """
    contract: DocumentSchema
