filepath = "C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 7/7.2/"

inp = input("Please enter the input file name: ")

print('\n')

text = open(filepath+inp, 'r').read()

res = ''

for cnt, line in enumerate(text.splitlines()):
    res += '/* ' + str(cnt) + ' */ ' + str(line) + '\n'

out = input("Please enter the output file name: ")

fw = open(filepath+out, 'w')
fw.write(res)
fw.close()

print("Task complete!")
