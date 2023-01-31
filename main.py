# This is a simple Python script.
# Homework from lesson 6.2 written by Kirill.S


from game_files.game_files_func import BasicWords
from game_files.players_history import Players
from my_input.my_input import InputAndCheckString
from config.config import FILE_FOR_WORDS, FILE_FOR_HISTORY, SCORE_FOR_RIGHT  # ,FILE_FOR_TEST
import random


def mix_string(input_str: str) -> str:
    """ mix letters in the string and return new string
    I know about random.shuffle(list), however I want to do this work by hands =)
    """
    new_mixed_sting: str = ""
    old_nonmixed_str_as_list: list = list(input_str.lower())
    size = len(input_str)
    for m_index in range(0, size):
        position = random.randint(0, size - m_index - 1)
        new_mixed_sting += str(old_nonmixed_str_as_list[position])
        del old_nonmixed_str_as_list[position]
    return new_mixed_sting


# MAIN block
if __name__ == '__main__':

    # init block
    my_words: BasicWords = BasicWords()
    my_players: Players = Players()
    # my_players.put_new_player_2_file(FILE_FOR_TEST, "Полуэкт", 500) # don't kill this string
    score_counter = 0   # guess pls, what is it =)

    # read all data from files
    my_words.read_words_from_file(FILE_FOR_WORDS)
    my_players.read_history_from_file(FILE_FOR_HISTORY)

    # name entering
    # current_player = input("Введите ваше имя")  # easy input from old version
    input_and_check_name: InputAndCheckString = InputAndCheckString()
    input_and_check_user_choose: InputAndCheckString = InputAndCheckString()
    input_and_check_name.input_while_correct("Введите ваше имя")

    # game section
    for effort in range(0, len(my_words.words)):
        word4game: str = mix_string(my_words.words[effort])
        print(word4game)
        input_and_check_user_choose.input_while_correct('try to find me >')
        if input_and_check_user_choose.input_string == my_words.words[effort]:
            print(f"Верно! Вы получаете {SCORE_FOR_RIGHT} очков.")
            score_counter += SCORE_FOR_RIGHT
        else:
            print(f'Неверно! Верный ответ – {my_words.words[effort]}.')

    # save section
    my_players.put_new_player_2_file(FILE_FOR_HISTORY, input_and_check_name.input_string, score_counter)

    # print statistics
    my_players.read_history_from_file(FILE_FOR_HISTORY)  # re-read file after last saving
    what_i_want_to_say: dict = my_players.get_statistic()

    print(f'Всего игр сыграно: {my_players.get_length()}')
    print(f'Максимальный рекорд у пользователя {what_i_want_to_say["name"]}: {what_i_want_to_say["score"]}')
