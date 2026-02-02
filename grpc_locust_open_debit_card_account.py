from locust import User, between, task

from clients.grpc.gateway.accounts.client import (AccountsGatewayGRPCClient,
                                                  build_accounts_gateway_locust_grpc_client)
from clients.grpc.gateway.users.client import (UsersGatewayGRPCClient,
                                               build_users_gateway_locust_grpc_client)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient

    create_user_response: CreateUserResponse
    open_debit_card_account_response: OpenDebitCardAccountResponse

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь происходит инициализация gRPC API клиентов и создание пользователя.
        """
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)

        self.create_user_response = self.users_gateway_client.create_user()
        self.user_id = self.create_user_response.user.id

    @task
    def open_debit_card_account(self) -> None:
        """
        Основная нагрузочная задача: создание дебетовой карты для пользователя.
        Метод будет многократно вызываться Locust-агентами.
        """
        self.accounts_gateway_client.open_debit_card_account(self.user_id)
