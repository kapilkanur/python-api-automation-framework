import requests

from api_client.api_response import APIResponse


class ApiRequestClient:

    def get(self, url):
        response = requests.get(url)
        return self.__get_response(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_response(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.__get_response(response)

    def __get_response(self, response):
        reason = response.reason
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception as e:
            print(e.args, e.__traceback__)
            as_dict = {}

        headers = response.headers

        return APIResponse(
            reason, status_code, text, as_dict, headers
        )
