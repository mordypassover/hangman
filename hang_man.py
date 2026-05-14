import random


def choose_game_word_from_list(lst):
    randum_word=random.choice(lst)
    return randum_word

def hied_word(word):
    return "_"* len(word)

def split_string_to_list(string):
    return list(string)

def hidden_word_in_list(word):
    hidden_word=hied_word(word)
    return split_string_to_list(hidden_word)

def reconnect_list_to_string(letter_list):
    reconnected=""
    for i in letter_list:
        reconnected+=i
    return reconnected

def show_game_status(cnt,hidden_split_word,wrong_letters):
    print(f"tris left: {cnt}, {reconnect_list_to_string(hidden_split_word)} , words used: {", ".join(wrong_letters)} ")

def get_letter(wrong_letters, hidden_list):
    user_letter= input("please enter a letter: ")

    if  not input_is_valid(user_letter) or (user_letter  in wrong_letters) :
        print("bad input")
        update_wrong_letters_list(user_letter, wrong_letters,hidden_list)
        return get_letter(wrong_letters, hidden_list)
    return user_letter

def input_is_valid(letter):
    return  letter.isalpha() and (len(letter) == 1)

def check_gues(letter,word,):
    return letter in list(word)

def update_hidden_list(letter,word,lst):
    for index, l in enumerate(word) :
        if letter == l:
            lst[index]=letter
    return lst

def update_wrong_letters_list(letter,wrong_list,hidden_list ):
    if (letter not in hidden_list)  and input_is_valid(letter):
         wrong_list.add(letter)
    return wrong_list

def update_lists(letter,word,hidden_list,wrong_letters_list):
    is_good_gues=check_gues(letter,word)
    if is_good_gues:
         update_hidden_list(letter,word,hidden_list)
    else:
        update_wrong_letters_list(letter,wrong_letters_list,hidden_list)
    return

def try_cnt_suber(cnt,letter, word):
    return cnt if check_gues(letter, word ) else cnt -1

def game_end(hidden_words,word ,tris):
    if hidden_words == list(word):
        print(f"congratulations! word:{word} you won with {tris} left!")
    else:
        print("you loose!")



def main():
    TRY_CNT = 10
    word_list = ['memory', 'ynet','ever']
    word=choose_game_word_from_list(word_list)
    hidden_letters_list=hidden_word_in_list(word)
    wrong_letters=set()



    while TRY_CNT > 0 and "_"  in hidden_letters_list:
        show_game_status(TRY_CNT, hidden_letters_list,wrong_letters)
        user_letter = get_letter(wrong_letters, hidden_letters_list)

        update_lists(user_letter,word,hidden_letters_list,wrong_letters)
        TRY_CNT=try_cnt_suber(TRY_CNT,user_letter,word)

    show_game_status(TRY_CNT, hidden_letters_list,wrong_letters)
    game_end(hidden_letters_list, word,TRY_CNT)

if __name__ == "__main__":
    main()
