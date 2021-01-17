# Problem Statement Determine the number of unique words contained in a text document. For example, the nursery rhyme “Mary had a little lamb” contains 57 unique words.
# Your task is to write a program that reads a text document and determines the number of
# unique words in it


# Part of Tupacs Ambitionz az A Ridah used as text

from collections import Counter

text = open('text.txt', 'r').read()

bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

text = text.lower()

for i in bad_chars:
    text = text.replace(i, '')

s1 = set(text.split())
print(len(s1))







