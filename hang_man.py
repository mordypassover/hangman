import random


def choose_game_word_from_list(lst):
    randum_index=random.randint(0,len(lst))
    return lst(randum_index)

def hied_word(word):
    pass

def split_string(string):
    pass

def hiden_word_inlist(word):
    pass

def reconnect_list_to_string(letter_list):
    pass

def show_game_status(cnt,hiden_split_word):
    pass

def get_letter():
    pass

def main():
    TRY_CNT=10
    word_list=[]
    word=choose_game_word_from_list(word_list)
    hiden_split_word=hiden_word_inlist(word)
    show_game_status(TRY_CNT, hiden_split_word)

