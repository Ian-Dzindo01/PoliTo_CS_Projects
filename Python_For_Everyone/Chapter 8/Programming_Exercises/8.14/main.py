bad_words_set = open('bad_words.txt', 'r').read().split()

text1 = open("text1.txt", 'r').read()

print(text1)

bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

text1 = text1.lower()

for i in bad_chars:
    text1 = text1.replace(i, '')


for word in bad_words_set:
    text1 = text1.replace(word, '!')


print(text1)
