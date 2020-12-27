# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:34:32 2020

@author: Haltuner
"""
import random

words = ["global" , "hub" , "turkish" , "english" , "world" , "mouse" , "house" , "home" , "computer" , "pencil"]
word = random.choice(words)      #random
guesses.number = 5
letters = []      
x = len(word)
z = list('_' * x)
print(' '.join(z), end='\n')

while guesses.number > 0:
    y = input("Guess a letter : ")
    if y in letters:
        print("Please guess a number that you did not predict before...")
        continueletters

    elif len(y) > 1:
        print("Please enter only one letter.")
        continue

    elif y not in word:   
        guesses.number -= 1
        print("Wrong guess!. {} you have left right to grain.".format(guesses.number))

    for i in range(len(word)):
        if y == word[i]:
            print("Right guess")
            z[i] = y
           word.append(y)
    print(' '.join(z), end='\n')

    if guesses.number == 0:
        print("You are out of guesswork. You lost.")
        break

    cevap = input("Do you want to guess the whole word? ['y' or 'n'] : ")

    if cevap == "e":
        guesses = input("Guess the whole word : ")
        if guesses == word:
            print("Congratulations...")
            break
        else:
           guesses.number -= 1
            print("Wrong guess. {} you have left right to grain.".format(guesses.number))
