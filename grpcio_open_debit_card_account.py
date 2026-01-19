import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (OpenDebitCardAccountRequest,
                                                                                 OpenDebitCardAccountResponse)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from tools.fakers import fake

# Устанавливаем соединение с gRPC-сервером по адресу localhost:9003
channel = grpc.insecure_channel("localhost:9003")

# Создаём gRPC-клиенты для UsersGatewayService и AccountsGatewayServiceStub
users_gateway_service = UsersGatewayServiceStub(channel)
account_gateway_service = AccountsGatewayServiceStub(channel)

# Формируем запрос на создание пользователя с рандомными данными
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)
# Отправляем запрос на создание пользователя и получаем ответ
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print('Create user response:', create_user_response)

# Достаём user_id для создания дебетового счёта
user_id = create_user_response.user.id

# Формируем запрос на создание дебетового счёта
create_debit_card_account_request = OpenDebitCardAccountRequest(user_id=user_id)

# Отправляем запрос на создание дебетового счёта и получаем ответ
open_debit_card_account_response: OpenDebitCardAccountResponse = account_gateway_service.OpenDebitCardAccount(create_debit_card_account_request)
print('Open debit card account response:', open_debit_card_account_response)
