import sys

keyword = (sys.argv[1]).lower()

files = []

for i in range(2, len(sys.argv)):
    files.append(sys.argv[i])

for i in range(len(files)):
    text = open(files[i], 'r').read()
    for line in text.splitlines():
        if keyword.upper() in line or keyword.lower() in line:
            print(files[i],':', line)







