# count the occurrence of each word in a text

from collections import Counter

text = open('text.txt', 'r').read()

bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

text = text.lower()

for i in bad_chars:
    text = text.replace(i, '')

d1 = Counter(text.split())
print(d1)

