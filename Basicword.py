class BasicWord:
    def __init__(self, word, words):
        self.word: str = word
        self.words: list = words

    def check_word(self, user_word):
        """
        - проверку введенного слова в списке допустимых подслов,
        :param user_word:
        :return:  bool
        """
        return user_word in self.words

    def get_statistics(self):
        """
         подсчет количества подслов
        :return: int
        """
        return len(self.words)

    def __repr__(self):
        return f"Составьте {self.get_statistics()} слов из слова '{self.word}'"
