# count the occurrence of each word in a text

from collections import Counter



bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

text = text.lower()

for i in bad_chars:
    text = text.replace(i, '')

d1 = Counter(text.split())

print(d1)



