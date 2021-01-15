# count the occurrence of each word in a text - print the 100 most common

from collections import Counter

text = open('text.txt', 'r').read()

bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

text = text.lower()

for i in bad_chars:
    text = text.replace(i, '')

d = Counter(text.split())

print(list(d.keys())[:100])
