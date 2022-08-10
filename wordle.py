# 1. sprawdzic czy slowo jest w 5 letterwords
# 2.wyswietlac poprawnie kolory czyli, jesli zielona litera jest juz pokazana to inna ta sama litera nie bedzie zolta


import random
from termcolor import colored

# with open("5letterwords.txt", "r") as f:
#     word = random.choice(f.readlines()).upper().strip()

word = 'MIDDY'

print("_____")

guess_word = '_____'

listed_words = '_____'

num = 0

print(word)

final_word = ''

# and word[i] != x[i]:

while num < 6:
    x = input("Podaj słowo: ").upper()
    if word == x:
        print('Zgadłeś słowo!', end=" ")
        print(colored(word, 'green'))
        break
    for i in range(len(word)):
        if word[i] == x[i]:
            print(colored(word[i], 'green'), end=' ')
            final_word += x[i]
        elif x[i] in word and word.count(x[i]) > final_word.count(x[i]):
            final_word += x[i]
            if x.count(x[i]) <= word.count(x[i]) :
                print(colored(x[i], 'yellow'), end=' ')
            else:
                print(colored(x[i], 'red'), end=' ')
        else:
            listed_words = guess_word
            print(colored(x[i], 'red'), end=' ')
    num += 1
    print()
    print(f"Zostało prób: {6 - num}")
    print(final_word)
    final_word = ''
    if num == 6:
        print(colored('Przegrałeś', 'red'), end="")
        print(', poprawne słowo to: ', end="")
        print(colored(word, 'green'))
