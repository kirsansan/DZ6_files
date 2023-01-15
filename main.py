# This is a sample Python script.


from game_files.game_files_func import BasicWords
from game_files.players_history import Players
from config.config import FILE_FOR_WORDS, FILE_FOR_HISTORY, FILE_FOR_TEST, SCORE_FOR_RIGHT
import random

def mix_string(input_str: str) -> str:
    """ mix letters in the string and return new string"""
    new_mixed_sting: str = ""
    old_nonmixed_str_as_list: list = list(input_str.lower())
    size = len(input_str)
    for m_index in range(0, size):
        position = random.randint(0, size - m_index -1)
        new_mixed_sting += str(old_nonmixed_str_as_list[position])
        del old_nonmixed_str_as_list[position]
    return new_mixed_sting

# Press the green my_wordsutton in the gutter to run the script.
if __name__ == '__main__':

    # init block
    my_words = BasicWords()

    my_words.read_words_from_file(FILE_FOR_WORDS)
    my_players: Players = Players()
    my_players.read_history_from_file(FILE_FOR_HISTORY)
    # print(my_players)
    # print(my_players.get_statistic())
    # my_players.put_new_player_2_file(FILE_FOR_TEST, "Полуэкт", 500)
    score_counter = 0


    # name entering
    current_player = input("Введите ваше имя")


    # game section

    for effort in range(0, len(my_words.words)):
        word4game: str = mix_string(my_words.words[effort])
        print(word4game)
        user_choose = input('try to find me >')
        if user_choose == my_words.words[effort]:
            print(f"Верно! Вы получаете {SCORE_FOR_RIGHT} очков.")
            score_counter += SCORE_FOR_RIGHT
        else:
            print(f'Неверно! Верный ответ – {my_words.words[effort]}.')

    # save section
    my_players.put_new_player_2_file(FILE_FOR_HISTORY, current_player, score_counter)

    # print statistics
    what_i_wand_to_sai: list = my_players.get_statistic()

    print(f'Всего игр сыграно: {my_players.get_length()}')
    print(f'Максимальный рекорд у пользователя {what_i_wand_to_sai[0]}: {what_i_wand_to_sai[1]}')

