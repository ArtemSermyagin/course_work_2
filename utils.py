import random

from Basicword import BasicWord
from config import URL
from database import DataBase
from random import shuffle


def load_random_word():
    """
    получает данные с внешнего ресурса,
    выберает случайное слово
    создаст экземпляр класса BasicWord
    :return: экземпляр класса BasicWord
    """
    database = DataBase(URL)
    words = database.load_remote_data()
    random.shuffle(words)
    if words:
        return BasicWord(words[0]["word"], words[0]['subwords'])


# print(load_random_word())
