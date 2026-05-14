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

def show_game_status(cnt,hiden_split_word,wrong_letters):
    print(f"trys left: {cnt}, {reconnect_list_to_string(hiden_split_word)} , words used: {", ".join(wrong_letters)} ")

def get_letter(wrong_letters, hiden_list):
    user_letter= input("please enter a letter: ")

    if not (user_letter.isalpha() and (len(user_letter) == 1) and (user_letter not in wrong_letters)) or user_letter  in  hiden_list:
        (print("bad input"))
        update_wrong_letters_list(user_letter, wrong_letters,hiden_list)
        return get_letter(wrong_letters, hiden_list)
    return user_letter


def check_gues(letter,word,):
    return letter in list(word)

def update_hiden_list(letter,word,lst):
    for index, l in enumerate(word) :
        if letter == l:
            lst[index]=letter
    return lst

def update_wrong_letters_list(letter,wrong_list,hiden_list ):
    if (letter not in hiden_list)  and len(letter) == 1:
         wrong_list.add(letter)
    return wrong_list

def update_lists(letter,word,hiden_list,wrong_letters_list):
    is_good_gues=check_gues(letter,word)
    if is_good_gues:
         update_hiden_list(letter,word,hiden_list)
    else:
        update_wrong_letters_list(letter,wrong_letters_list,hiden_list)
    return


def main():
    TRY_CNT = 10
    word_list = ['wert', 'qwertyh','wertgv']
    word=choose_game_word_from_list(word_list)
    hiden_letters_list=hiden_word_in_list(word)
    wrong_letters=set()



    while TRY_CNT > 0 and "_"  in hiden_letters_list:
        show_game_status(TRY_CNT, hiden_letters_list,wrong_letters)
        user_letter = get_letter(wrong_letters, hiden_letters_list)

        update_lists(user_letter,word,hiden_letters_list,wrong_letters)
        TRY_CNT-=1
main()