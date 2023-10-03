from Basicword import BasicWord
from Player import Player
from utils import load_random_word


def main():
    user_name = input("Ввведите имя игрока: ")
    print(f"\nПривет, {user_name}!")
    basic_word = load_random_word()
    print(basic_word)
    print("Слова должны быть не короче 3 букв")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print("Поехали, ваше первое слово?")
    player = Player(user_name)
    print(basic_word.words)
    user_word = input("Введите слово: ")
    while True:
        if len(user_word) < 3:
            print("Слишком короткое слово")
        elif not basic_word.check_word(user_word):
            print("неверно")
        elif player.verification_word(user_word):
            print("Слово уже использовано")
        else:
            player.append_used_word(user_word)
            print("верно")
        if user_word.lower() in ["stop", "стоп"] or basic_word.get_statistics() == player.get_words_used():
            print(f"Игра завершена, вы угадали {player.get_words_used()} слов!")
            break
        user_word = input("Введите слово: ")


if __name__ == "__main__":
    main()
