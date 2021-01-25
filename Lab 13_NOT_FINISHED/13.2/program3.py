l = [i for i in range(2000, 3201) if i%5 != 0 and i%7 == 0]

s = str(l)

s = s[1:-1]

fw = open("result3.txt", 'w')
fw.write(s)
fw.close()

