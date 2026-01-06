import json
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.cards.client import build_cards_http_gateway_client
from clients.http.gateway.users.client import build_users_gateway_http_client


users_gateway_client = build_users_gateway_http_client()
cards_gateway_client = build_cards_http_gateway_client()
accounts_gateway_client = build_accounts_gateway_http_client()


create_user_response = users_gateway_client.create_user()
print('Create user response: ', json.dumps(create_user_response, indent=4))

user_id = create_user_response['user']['id']
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(user_id)
print('Open debit card response: ', json.dumps(open_debit_card_account_response, indent=4))

account_id = open_debit_card_account_response['account']['id']
issue_physical_card_account = cards_gateway_client.issue_physical_card(user_id, account_id)
print('Issue physical card response: ', json.dumps(issue_physical_card_account, indent=4))
