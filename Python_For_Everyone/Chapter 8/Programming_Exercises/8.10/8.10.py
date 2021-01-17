text1 = open("text1.txt", 'r').read()
text2 = open("text2.txt", 'r').read()


bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']


text1 = text1.lower()
text2 = text2.lower()


for i in bad_chars:
    text1 = text1.replace(i, '')


for i in bad_chars:
    text2 = text2.replace(i, '')

s1 = set(text1.split())
s2 = set(text2.split())

print("The words that are common to the texts are the following: ", list(s1&s2))





