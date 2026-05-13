import random


def choose_game_word_from_list(lst):
    randum_index=random.choice(lst)
    return randum_index

def hied_word(word):
    return "_"* len(word)

def split_string_to_list(string):
    return list(string)

def hiden_word_in_list(word):
    hiden_word=hied_word(word)
    return split_string_to_list(hiden_word)

def reconnect_list_to_string(letter_list):
    reconnected=""
    for i in letter_list:
        reconnected+=i
    return reconnected

def show_game_status(cnt,hiden_split_word):
    print(f"{cnt} {reconnect_list_to_string(hiden_split_word)}")

def get_letter(wrong_letters=[None]):
    user_letter= input("please enter a letter: ")
    return user_letter if user_letter.isalpha() and len(user_letter)==1 and user_letter not in wrong_letters  else (print("bad input"),get_letter())

def check_gues(letter,word,):
    return letter in word

def update_hiden_list(letter,word,lst):
    for index, l in enumerate(word) :
        if letter == l:
            lst[index]=letter
    return lst

def update_wrong_letters_list(letter,lst):
    return lst.append(letter)

def update_lists(letter,word,hiden_list,wrong_letters_list):
    is_good_gues=check_gues(letter,word)
    return update_hiden_list(letter,word,hiden_list) if is_good_gues else  update_wrong_letters_list(letter,wrong_letters_list)


def main():
    TRY_CNT=10
    word_list=['wert','qwertyh','wertgv']
    word=choose_game_word_from_list(word_list)
    hiden_letters_list=hiden_word_in_list(word)
    wrong_letters=[]
    show_game_status(TRY_CNT, hiden_letters_list)
    while TRY_CNT > 0 and "_" not in word_list:
        user_letter=get_letter(wrong_letters)
    