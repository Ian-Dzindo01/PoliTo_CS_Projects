import inflect

d = {}
p = inflect.engine()

for i in range(1,6):
    d[i] = p.number_to_words(i)


for i in d.values():
    print(i)

