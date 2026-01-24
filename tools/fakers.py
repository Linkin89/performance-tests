from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper
from faker import Faker
import time
from faker.providers.python import TEnum


class Fake:
    """Класс для генерации случайных тестовых данных с использованием библиотеки Faker"""

    def __init__(self, faker: Faker):
        """:param faker: Экземпляр класса Faker"""
        self.faker = faker

    def enum(self, value: type[TEnum]) -> TEnum:
        """
        Выбирает случайное значение из enum-типа

        :param value: Enum-класс для генерации значения
        :return: Случайное значение из Enum-класса
        """
        return self.faker.enum(value)

    def email(self) -> str:
        """
        Генерирует случайный email

        :return: Cлучайный email
        :rtype: str
        """
        return f"{time.time()}.{self.faker.email()}"

    def category(self) -> str:
        """
        Генерирует случайную категорию покупки из предопределённого списка

        :return: Случайная категория покупки
        :rtype: str
        """
        return self.faker.random_element([
            "gas",
            "taxi",
            "tolls",
            "water",
            "beauty",
            "mobile",
            "travel",
            "parking",
            "catalog",
            "internet",
            "satellite",
            "education",
            "government",
            "healthcare",
            "restaurants",
            "electricity",
            "supermarkets",
        ])

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        :return: Случайная фамилия.
        :rtype: str
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        :rtype: str
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество/среднее имя.

        :return: Случайное отчество.
        :rtype: str
        """
        return self.faker.first_name()

    def phone_number(self) -> str:
        """
        Генерирует случайный номер телефона

        :return: Случайный номер телефона
        :rtype: str
        """
        return self.faker.phone_number()

    def float(self, start: int = 1, end: int = 100) -> float:
        """
        Генерирует случайное число с плавающей запятой в заданном диапазоне

        :param start: Нижняя граница генерируемого числа (включительно)
        :type start: int
        :param end: Верхняя граница генерируемого числа (включительно)
        :type end: int
        :return: Случайное число с плавающей запятой в пределах start и end
        :rtype: float
        """
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        """
        Генерирует случайную стоимость

        :return: Сумма от 1 до 100
        :rtype: float
        """
        return self.float(1, 100)

    def proto_enum(self, value: EnumTypeWrapper) -> int:
        """
        Выбирает случайное значение из proto enum-типа.

        :param value: Proto enum-класс для генерации значения.
        :return: Случайное значение из перечисления.
        """
        return self.faker.random_element(value.values())


fake = Fake(faker=Faker())
