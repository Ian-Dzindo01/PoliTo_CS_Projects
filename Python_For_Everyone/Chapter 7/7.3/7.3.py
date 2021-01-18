import sys

filepath = "C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 7/7.3/"

if len(sys.argv) < 3:
    print("Please rerun the program and provide a name for both the input and the output file!")
    sys.exit()

inp = sys.argv[1]

text = open(filepath+inp, 'r').read()

res = ''

for cnt, line in enumerate(text.splitlines()):
    res += '/* ' + str(cnt) + ' */ ' + str(line) + '\n'

out = sys.argv[2]

fw = open(filepath+out, 'w')
fw.write(res)
fw.close()

print("Task complete!")
