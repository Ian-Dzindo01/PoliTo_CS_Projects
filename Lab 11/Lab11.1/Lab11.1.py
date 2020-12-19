import string

text = open('OhNo.txt', 'r').read()
text = text.translate(str.maketrans('', '', string.punctuation))

cnt = {}

for line in text.splitlines():
    for word in line.split():
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1

print(cnt, '\n')

print("The most common 100 words are: \n")

for w in sorted(cnt, key=cnt.get, reverse=True)[:100]:
    print(w, cnt[w])
