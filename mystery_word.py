import random


with open("/usr/share/dict/words", "r") as f:
    list_of_words = []

    for line in f:
        list_of_words += line.split()

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
    random_word = random.choice(three_lists())
    print(random_word)

def choose_difficulty():
    dif_choice = input("chose easy/normal/hard mode: ").lower()
    if dif_choice == 'easy':
        return 'easy'
    elif dif_choice == 'normal':
        return 'normal'
    else:
        return 'hard'

def main():
    random_word()
    pass










main()
# if __name__ == "__main__":
#     main()
