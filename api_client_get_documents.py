import json
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client


users_gateway_client = build_users_gateway_http_client()
account_gateway_client = build_accounts_gateway_http_client()
documents_gateway_client = build_documents_gateway_http_client()


response_create_user = users_gateway_client.create_user()
print('Create user response: ', json.dumps(response_create_user, indent=4))

user_id = response_create_user['user']['id']
response_open_credit_card_account = account_gateway_client.open_credit_card_account(user_id)
print('Open credit card account response: ', json.dumps(response_open_credit_card_account, indent=4))

account_id = response_open_credit_card_account['account']['id']
response_get_tariff_document = documents_gateway_client.get_tariff_document(account_id)
print('Get tariff document response: ', json.dumps(response_get_tariff_document, indent=4))

response_get_contract_document = documents_gateway_client.get_contract_document(account_id)
print('Get contract document response: ', json.dumps(response_get_contract_document, indent=4))
