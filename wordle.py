#! 1. tablice ze slowami, taka sama dlugosc slowa (10) !
#! 2. losowanie slowa z tablicy
# 3. warunki gry: na start wyswietla sie 5 pustych kratek
# 4. uzytkownik wpisuje litere, jesli ona jest na wlasciwym miejscu to ja pokazuje
# 5. po 6 nietrafionych strzałach gracz odpada


import random

words = ['AGENT', 'COACH', 'EARTH', 'WATER', 'FAIRY', 'GHOST', 'STEEL', 'GRASS', 'DRAKE', 'CLOCK']

word = random.choice(words)


print(word)

print("_____")

guess_word = '_____'

listed_words = '_____'

num = 0

while num < 6 and '_' in listed_words:
    x = input("Podaj słowo: ").upper()
    for i in range(len(word)):
        if word[i] == x[i]:
            temp = list(guess_word)
            temp[i] = word[i]
            listed_words = "".join(temp)
            guess_word = listed_words
        else:
            listed_words = guess_word
    num += 1
    print(f"Zostało prób: {6 - num}")
    print(listed_words)

if '_' in listed_words:
    print('Przegrales')
else:
    print("Wygrales")
