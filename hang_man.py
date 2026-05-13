import random


def choose_game_word_from_list(lst):
    randum_index=random.randint(0,len(lst))
    return lst(randum_index)

def hied_word(word):
    return "_"* len(word)

def split_string_to_list(string):
    return list(string)

def hiden_word_in_list(word):
    hiden_word=hied_word(word)
    return split_string_to_list(hiden_word)

def reconnect_list_to_string(letter_list):
    pass

def show_game_status(cnt,hiden_split_word):
    print(f"{cnt} {reconnect_list_to_string(hiden_split_word)}")

def get_letter():
    pass

def main():
    TRY_CNT=10
    word_list=[]
    word=choose_game_word_from_list(word_list)
    hiden_letters_list=hiden_word_in_list(word)
    show_game_status(TRY_CNT, hiden_letters_list)

