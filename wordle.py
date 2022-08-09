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

while num < 6:
    x = input("Podaj słowo: ").upper()
    if word == x:
        print('Zgadłeś słowo!', end=" ")
        print(colored(word, 'green'))
        break
    for i in range(len(word)):
        if word[i] == x[i]:
            print(colored(word[i], 'green'), end=' ')
        elif x[i] in word:
            print(colored(x[i], 'yellow'), end=' ')
        else:
            listed_words = guess_word
            print(colored(x[i], 'red'), end=' ')
    num += 1
    print()
    print(f"Zostało prób: {6 - num}")
    print('_____')
    if num == 6:
        print(colored('Przegrałeś', 'red'), end="")
        print(', poprawne słowo to: ', end="")
        print(colored(word, 'green'))
