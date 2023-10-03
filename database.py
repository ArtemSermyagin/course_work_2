import json
import requests
from requests import Response, get

from config import URL


class DataBase:
    def __init__(self, URL: str):
        self.URL = URL


    def get_response(self) -> Response:
        """
        получает ответ от сервера
        :return: ответ
        """
        return get(self.URL)

    def load_remote_data(self) -> list[dict]:
        """
        :return: возвращает закодированное в json
        """
        response = self.get_response()
        return response.json()
