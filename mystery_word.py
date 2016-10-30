import random

with open("/usr/share/dict/words", "r") as f:
    list_of_words = []

    for line in f:
        list_of_words += line.split()

def get_guess_letter():
    guess_letter = input("guess a letter: ").lower()
    return guess_letter

def guess_in_word(guess, master_word, good_guess_list, bad_guess_list):
    guess = get_guess_letter().lower()
    success = 0
    # list_of_guesses += guess
    # print(list_of_guesses)
    if guess in master_word:
        print("yes")
        success += 1
        return word_maker(guess, master_word, good_guess_list, bad_guess_list)
    else:
        print("NO")

        return word_maker(guess, master_word, good_guess_list, bad_guess_list)


def guess_not_in(guess):
    if guess not in bad_guess_list:
        bad_guess_list += guess
        return bad_guess_list
    else:
        print(bad_guess_list)
        return bad_guess_list

def guess_in(guess):
    good_guess_list += guess
    return good_guess_list

def draw_word(word):
    print(len(word) * "_ ")

# def printer(guess, master_word):
#     replace_value = master_word.index(guess)
#     gap_word = len(master_word) * "_"
#     gap_word = gap_word[:replace_value] + guess + gap_word[replace_value:]
#     master_word = master_word[:replace_value] + "_" + master_word[replace_value + 1:]
#     while guess in master_word:
#         gap_word
#     # while guess in master_word:


    # print(gap_word)

def word_maker(guess, master_word, good_guess_list, bad_guess_list):
    semi_string = ''
    i = 0
    for character in master_word:
        i += 1
        if character == guess:
            #guess_in(guess)
            semi_string += character
            #print(semi_string)
            if i == len(master_word):
                print(semi_string)
                good_guess_list += guess
                print(bad_guess_list)
                print(good_guess_list)
                return guess_in_word(guess, master_word, good_guess_list, bad_guess_list)
        else:
            semi_string += '_ '
            if guess in master_word:
                if i == len(master_word):
                    good_guess_list += guess
                    print(semi_string)
                    return guess_in_word(guess, master_word, good_guess_list, bad_guess_list)
            else:
                bad_guess_list += guess

                print(bad_guess_list)
                print(good_guess_list)
                guess_in_word(guess, master_word, good_guess_list, bad_guess_list)
                print(semi_string)
    #print(semi_string)


def three_lists():
    easy_word_list = []
    normal_word_list = []
    hard_word_list = []
    dif_choice = choose_difficulty()
    for word in list_of_words:
        if len(word) == 4 or len(word) == 5:
            easy_word_list += word.split()
        elif len(word) == 6:
            easy_word_list += word.split()
            normal_word_list += word.split()
        elif len(word) == 7:
            normal_word_list += word.split()
        elif len(word) == 8:
            normal_word_list += word.split()
            hard_word_list += word.split()
        else:
            hard_word_list += word.split()
    if dif_choice == 'easy':
        return easy_word_list
    elif dif_choice == 'normal':
        return normal_word_list
    else:
        return hard_word_list

def random_word():
    random_word = random.choice(three_lists()).lower()
    print(random_word)
    print("your secret word contains {} letters.".format(len(random_word)) )
    return(random_word)

def choose_difficulty():
    dif_choice = input("chose easy/normal/hard mode: ").lower()
    if dif_choice == 'easy':
        return 'easy'
    elif dif_choice == 'normal':
        return 'normal'
    else:
        return 'hard'

def main():
    bad_guess_list = []
    good_guess_list = []
    list_of_guesses = []
    master_word = random_word()
    guess = ''
    draw_word(master_word)
    guess_in_word(guess, master_word, good_guess_list, bad_guess_list)








main()
# if __name__ == "__main__":
#     main()
