import random
from termcolor import colored

language = input("Wybierz 'pl' albo 'eng': ").lower()


def list_of_words():
    global language
    while language not in ["pl", "eng"]:
        language = input("Wybierz 'pl' albo 'eng': ").lower()
    if language == 'eng':
        with open("5letterwordseng.txt", "r") as f:
            check_words = f.read().upper().splitlines()
            return check_words
    elif language == 'pl':
        with open("5letterspl.txt", "r", encoding="utf-8") as f:
            ch_words = f.read().upper().splitlines()
            check_words = [letter for letter in ch_words if len(letter) == 5]
            return check_words


var_of_words = list_of_words()

word = random.choice(var_of_words).upper().strip()

num = 0

while num < 6:
    final_word = input("Podaj słowo 5 literowe: ").upper()
    while final_word not in var_of_words:
        final_word = input("Podaj poprawne słowo 5 literowe: ").upper()
    if word == final_word:
        print('Zgadłeś słowo!', end=" ")
        print(colored(word, 'green'))
        break

    dict_of_letters = {}

    for i in word:
        dict_of_letters[i] = word.count(i)

    for i in range(len(final_word)):
        if final_word[i] in dict_of_letters and dict_of_letters[final_word[i]] > 0:
            if final_word[i] == word[i]:
                dict_of_letters[final_word[i]] -= 1

    for i in range(len(final_word)):
        if final_word[i] == word[i]:
            print(colored(final_word[i], 'green'), end=' ')
        elif final_word[i] in dict_of_letters and dict_of_letters[final_word[i]] > 0:
            print(colored(final_word[i], 'yellow'), end=' ')
            dict_of_letters[final_word[i]] -= 1
        else:
            print(colored(final_word[i], 'red'), end=' ')
    num += 1
    print()
    print(f"Zostało prób: {6 - num}")
    final_word = ''
    if num == 6:
        print(colored('Przegrałeś', 'red'), end="")
        print(', poprawne słowo to: ', end="")
        print(colored(word, 'green'))

