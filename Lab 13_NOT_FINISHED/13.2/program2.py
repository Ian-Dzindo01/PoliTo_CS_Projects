l = [i for i in range(2000, 3201) if not(i%7) and i%5]

s = str(l)

s = s[1:-1]

fw = open("result2.txt", 'w')
fw.write(s)
fw.close()
