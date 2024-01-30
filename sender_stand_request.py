import configuration
import requests
import data

def get_Authorization(Authorization):
    current_body = data.headers.copy()
    current_body["Authorization"] = Authorization
    return current_body



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                 headers=data.headers)

def get_token():
    response = post_new_user(data.user_body)
    token = response.json()
    authToken = token["authToken"]
    bearerToken = 'Bearer ' + authToken
    return get_Authorization(bearerToken)

def post_new_client_kits(body):
    header = get_token()
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS_PATH, json=body, headers=header)

response = post_new_client_kits(data.kits_body)
print(response.status_code)


