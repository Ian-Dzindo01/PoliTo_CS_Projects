l = []

for i in range(2000, 3201):
    if i%7 == 0 and i%5 != 0:
        l.append(i)

s = str(l)

s = s[1:-1]

fw = open("result1.txt", 'w')
fw.write(s)
fw.close()


