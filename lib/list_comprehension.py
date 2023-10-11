#!/usr/bin/env python3
l = [1, 2, 3, 4, 5]



def return_evens(num_list):
    # evens = []
    # for n in num_list:
    #     if n % 2 == 0:
    #         evens.append(n)
    evens = [n for n in num_list if n % 2 == 0 ]
    return evens

    

def make_exclamation(sentence_list):
    exclaim = [sent + "!" for sent in sentence_list if len(sent) > 1]
    return exclaim

k = ["Hello", "I'm doing great", "Python is fun"]