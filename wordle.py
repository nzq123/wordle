# 1. sprawdzic czy slowo jest w 5 letterwords
# 2.wyswietlac poprawnie kolory czyli, jesli zielona litera jest juz pokazana to inna ta sama litera nie bedzie zolta


import random
from termcolor import colored

with open("5letterwords.txt", "r") as f:
    word = random.choice(f.readlines()).upper().strip()


print("_____")

guess_word = '_____'

listed_words = '_____'

num = 0


final_word = ''

# and word[i] != x[i]:

while num < 6:
    x = input("Podaj słowo: ").upper()
    if word == x:
        print('Zgadłeś słowo!', end=" ")
        print(colored(word, 'green'))
        break
    # for i in range(len(word)):
    #     if x[i] in word and word[i] != x[i]:
    for i in range(len(word)):
        if x[i] in word and word[i] == x[i]:
            final_word += x[i]
        elif x[i] in word and word.count(x[i]) > final_word.count(x[i]):
            final_word += x[i]
        else:
            final_word += x[i]

    dict_of_letters = {}

    for i in word:
        dict_of_letters[i] = word.count(i)

    result = [1, 2, 3, 4, 5]

    for i in range(len(final_word)):
        if final_word[i] in dict_of_letters and dict_of_letters[final_word[i]] > 0:
            if final_word[i] == word[i]:
                dict_of_letters[final_word[i]] -= 1

    for i in range(len(final_word)):
        if final_word[i] in dict_of_letters:
            if final_word[i] == word[i]:
                result[i] = final_word[i]

    for i in range(len(final_word)):
        if result[i] == word[i]:
            print(colored(final_word[i], 'green'), end=' ')
        elif final_word[i] in dict_of_letters and dict_of_letters[final_word[i]] > 0:
            print(colored(final_word[i], 'yellow'), end=' ')
            dict_of_letters[final_word[i]] -= 1
        else:
            print(colored(final_word[i], 'red'), end=' ')
    num += 1
    print()
    print(f"Zostało prób: {6 - num}")
    print(final_word)
    final_word = ''
    if num == 6:
        print(colored('Przegrałeś', 'red'), end="")
        print(', poprawne słowo to: ', end="")
        print(colored(word, 'green'))

