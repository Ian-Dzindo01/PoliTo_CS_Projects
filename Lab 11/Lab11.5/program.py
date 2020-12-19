bad_words = ['nigga', 'Nigga', 'Niggas', 'bitch', 'Bitch', 'bitches', 'Bitches', 'shit', 'Shit', 'Sex', 'sex', 'pussy', 'Pussy']

text = open('bad_text.txt', 'r').read()

def replaceWithAsterisk(text, word):
    return text.replace(word, '*'*len(word))

for word in bad_words:
    text = text.replace(word, '*'*len(word))


fw = open('good_text.txt', 'w')
fw.write(text)
fw.close()
