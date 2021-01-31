import sys

with open(sys.argv[1], 'r') as file:
    data = file.read()

with open(sys.argv[2], 'w') as file:
    file.write(data)
