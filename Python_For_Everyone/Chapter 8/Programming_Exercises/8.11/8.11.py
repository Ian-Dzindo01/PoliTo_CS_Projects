import string

text1 = open("text1.txt", 'r').read()

bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

text1 = text1.lower()

for i in bad_chars:
    text1 = text1.replace(i, '')

s1 = set(text1.split())

d = {}
temp = set()

for letter in list(string.ascii_lowercase):
    for word in s1:
        if letter in word:
            temp.add(word)

    d[letter] = list(temp)
    temp.clear()


for key in d:
    print(key, ': ', d[key], '\n')
