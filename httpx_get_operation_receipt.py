import json
from time import time
import httpx

from clients.http.gateway.cards.client import CardsGatewayHTTPClient
from clients.http.gateway.users.client import UsersGatewayHTTPClient


name = f"vadim{time()}"
new_user = {
    "email": f"{name}@example.com",
    "lastName": name,
    "firstName": name,
    "middleName": name,
    "phoneNumber": "32132"
}

client = httpx.Client(base_url='http://localhost:8003')

response_create_user = client.post(url='/api/v1/users',
                                   json=new_user)
response_create_user_data = response_create_user.json()
user_id = response_create_user_data['user']['id']

request_open_credit_card_data = {
    'userId': user_id
}

response_open_credit_card = client.post('/api/v1/accounts/open-credit-card-account',
                                        json=request_open_credit_card_data)

response_open_credit_card_data = response_open_credit_card.json()
credit_card_account_id = response_open_credit_card_data['account']['id']
virtual_credit_card_id = response_open_credit_card_data['account']['cards'][0]['id']

new_purchase_operation = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": virtual_credit_card_id,
    "accountId": credit_card_account_id
}

response_make_purchase_operation = client.post('/api/v1/operations/make-purchase-operation',
                                               json=new_purchase_operation)
response_make_purchase_operation_data = response_make_purchase_operation.json()
purchase_operation_id = response_make_purchase_operation_data['operation']['id']

response_operation_receipt = client.get(f'/api/v1/operations/operation-receipt/{purchase_operation_id}')

pretty_json_response_operation_receipt = json.dumps(response_operation_receipt.json(), indent=4)
print("Response operation receipt: ", pretty_json_response_operation_receipt)
