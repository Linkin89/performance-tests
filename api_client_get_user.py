from clients.http.gateway.users.client import build_users_gateway_http_client


users_gateway_client = build_users_gateway_http_client()

create_user_response = users_gateway_client.create_user()

user_id = create_user_response['user']['id']
response_get_user = users_gateway_client.get_user(user_id)
print(response_get_user)
