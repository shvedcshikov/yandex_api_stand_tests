import configuration
import requests

from configuration import USERS_TABLE_PATH


def qet_user_table():
    return requests.get(configuration.URL_SERVICE + USERS_TABLE_PATH)

response=qet_user_table()

print(response.status_code)
print(response.headers)