#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for n in num_list:
        if n % 2 == 0:
            evens.append(n)
    return evens
return_evens([0, 1, 3, 5, 7, 8, 9])



def make_exclamation(sentence_list):
    sentences = []
    for s in sentence_list:
        s = (s + '!')
        sentences.append(s)
    return sentences
make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))