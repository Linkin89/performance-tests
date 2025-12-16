from time import time
import httpx


name = f"vadim{time()}"
new_user = {
    "email": f"{name}@example.com",
    "lastName": name,
    "firstName": name,
    "middleName": name,
    "phoneNumber": "32132"
}

response_create_user = httpx.post(url='http://localhost:8003/api/v1/users',
                                  json=new_user)

response_create_user_data = response_create_user.json()
user_id = response_create_user_data['user']['id']
print("Status code: ", response_create_user.status_code)
print("Response create user: ", response_create_user_data)

response_data = {"userId": user_id}
response_create_account = httpx.post(url='http://localhost:8003/api/v1/accounts/open-deposit-account',
                                     json=response_data,
                                     timeout=10)

response_create_account_data = response_create_account.json()
print("Status code: ", response_create_account.status_code)
print("Response create account: ", response_create_account_data)
