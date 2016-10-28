import random

with open("/usr/share/dict/words", "r") as f:
    list_of_words = []

    for line in f:
        list_of_words += line.split()

def get_guess_letter():
    guess_letter = input("guess a letter: ").lower()
    return guess_letter

def guess_in_word():
    wordword = random_word()
    guess_letter = get_guess_letter().lower()
    #while len(wordword) >
    if guess_letter in wordword:
        print("yes")
        print (guess_in(guess_letter))
        return (guess_in(guess_letter))
        return True
    else:
        print("NO")
        print (guess_not_in(guess_letter))
        return (guess_not_in(guess_letter))
        return False


def guess_not_in(guess_letter):
    bad_guess_list = []
    bad_guess_list += guess_letter
    return bad_guess_list

def guess_in(guess_letter):
    good_guess_list = []
    good_guess_list += guess_letter
    return good_guess_list

def draw_word():
    print(len(random_word()) * "_ ")


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
    draw_word()
    get_guess_letter()
    guess_in_word()










main()
# if __name__ == "__main__":
#     main()
