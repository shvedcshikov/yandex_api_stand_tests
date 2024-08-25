import configuration
import requests

from configuration import LOG_MAIN_PATH



def qet_logs():
    return requests.get(configuration.URL_SERVICE + LOG_MAIN_PATH,params={"count":20})

response=qet_logs()

print(response.status_code)
print(response.headers)