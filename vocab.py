#!/usr/bin/python
# Alex Eames RasPi.TV http://raspi.tv/?p=9652
from __future__ import print_function
import random

try:
   # Python2
   input = raw_input
except NameError:
   # Python3
   pass

iterations = 100
correction_factor = 6.75
recognised = 0
unknown_words = []

# Open the word list and read into Python list
results = list(open("wordlist.txt", "r"))
clean_lines = [x.strip() for x in results] # remove \n line ends
lines = len(clean_lines)

for x in range(iterations):
    selection = random.randint(0, lines)
    print(clean_lines[selection])
    if x % 10 == 0:
        answer = input("<Enter> = recognise, anything else = don't recognise")
    else:
        answer = input()
    if answer == "":
        recognised += 1
    else:
        unknown_words.append(clean_lines[selection])

vocab = int(recognised / float(iterations) * lines)

print("recognised: ", recognised, "out of ", iterations)
print("that's ", recognised / float(iterations) * 100, "%")
print("Your 'Scrabble list' vocabulary is: ", vocab)
print("Your 'Corrected'     vocabulary is: ", int(vocab / correction_factor))
print("Here are the words you said you didn't know...")

add_unknowns = open("unknown_words.txt", "a")
for word in unknown_words:
    print(word)
    add_unknowns.write(word+"\n")

add_unknowns.close()
