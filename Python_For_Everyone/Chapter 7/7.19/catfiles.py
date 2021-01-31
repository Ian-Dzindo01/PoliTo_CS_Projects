import sys

data = ''

for i in range(1, len(sys.argv)-1):
    with open(sys.argv[i], 'r') as file:
        data += file.read()

with open(sys.argv[len(sys.argv)-1], 'w') as file:
    file.write(data)


