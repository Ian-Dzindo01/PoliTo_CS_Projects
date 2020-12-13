from collections import defaultdict

try:
    fr = open('report.txt', 'r')
except FileNotFoundError as e:
    print(e)
else:
    text = fr.read()
    fr.close()


print(text)

d1 = defaultdict(int)

try:
    for line in text.splitlines():
        temp = line.split(';')
        d1[temp[1]] += int(temp[2])

except Exception:
    print("The text is in the wrong format.")

for key in d1:
    print(key, '=', d1[key])
