import random


with open("/usr/share/dict/words", "r") as f:
    list_of_words = []
    for line in f:
        list_of_words += line.split()


def get_guess_letter():
    guess_letter = input("guess a letter: ").lower()
    while True:
        if guess_letter.isalpha():
            if len(guess_letter) == 1:
                return guess_letter
            else:
                print("you entered too many letters")
                guess_letter = input("guess a letter: ").lower()
        else:
            print("please enter a LETTER")
            guess_letter = input("guess a letter: ").lower()


def draw_word(word):
    print(len(word) * "_ ")
    return(len(word) * "_ ")


def fake_function(word):
    return word


def word_maker(guess, master_word, good_guess_list, bad_guess_list):
    semi_string = ''
    i = 0
    if len(bad_guess_list) == 8:
        lose(master_word)
        replay_game()
    if guess in good_guess_list:
        print("you already guessed that letter.")
    for character in master_word:
        i += 1
        if character == guess:
            semi_string += character
            semi_string += ' '
            if i == len(master_word):
                print("Bad Guesses: ")
                print(bad_guess_list)
                print(semi_string)
                good_guess_list += guess
                guess = get_guess_letter()
                return word_maker(guess, master_word, good_guess_list, bad_guess_list)
                if "_" not in semi_string:
                    win(master_word)
                    replay_game()
        else:
            if character in good_guess_list:
                semi_string += character
                semi_string += ' '
            else:
                semi_string += '_ '
            if guess in master_word:
                if i == len(master_word):
                    print("you have {} guesses left: ".format(8 - len(bad_guess_list)))
                    good_guess_list += guess
                    print("Bad Guesses: ")
                    print(bad_guess_list)
                    print(semi_string)
                    if "_" not in semi_string:
                        win(master_word)
                        replay_game()
                    guess = get_guess_letter()
                    return word_maker(guess, master_word, good_guess_list, bad_guess_list)

            elif i < len(master_word):
                continue
            else:
                if "_" not in semi_string:
                    win(master_word)
                    replay_game()
                if guess not in bad_guess_list:
                    bad_guess_list += guess
                    if len(bad_guess_list) == 8:
                        lose(master_word)
                        replay_game()
                else:
                    print("you already guessed that letter")
                print("Bad Guesses: ")
                print(bad_guess_list)
                print("you have {} guesses left: ".format(8 - len(bad_guess_list)))
                print(semi_string)
                guess = get_guess_letter()
                word_maker(guess, master_word, good_guess_list, bad_guess_list)
    return semi_string


def lose(master_word):
    print("you lose. word was: {}".format(master_word))


def win(master_word):
    print("YOU WIN! word was: {}".format(master_word))


def replay_game():
    play_again = input("would you like to play again? Y/n ".lower())
    if play_again == 'y':
        main()
    else:
        print("thanks for playing")
        exit()


def three_lists(dif_choice):
    easy_word_list = []
    normal_word_list = []
    hard_word_list = []
    # dif_choice = choose_difficulty()
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
        elif len(word) > 8:
            hard_word_list += word.split()
    if dif_choice == 'easy':
        return easy_word_list
    elif dif_choice == 'normal':
        return normal_word_list
    else:
        return hard_word_list


def random_word(dif_choice):
    random_word = random.choice(three_lists(dif_choice)).lower()
    print("your secret word contains {} letters.".format(len(random_word)))
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
    dif_choice = choose_difficulty()
    master_word = random_word(dif_choice)
    draw_word(master_word)
    guess = get_guess_letter()
    word_maker(guess, master_word, good_guess_list, bad_guess_list)

if __name__ == "__main__":
    main()
