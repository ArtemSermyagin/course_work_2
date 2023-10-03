class Player:
    def __init__(self, username):
        self.username = username
        self.words_used = []

    def get_words_used(self):
        """
        получение количества использованных слов
        :return: (возвращает int)
        """
        return len(self.words_used)

    def append_used_word(self, used_word):
        """
        добавляет используемое слово
        :param used_word:
        :return:
        """
        self.words_used.append(used_word)

    def verification_word(self, word):
        """
        проверка использования данного слова до этого (возвращает bool).
        :return: True or False
        """
        return word in self.words_used

    def __repr__(self):
        return self.username
