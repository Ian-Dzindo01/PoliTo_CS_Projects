import sys

filepath = "C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 7/7.9/"     # you will need to change this filepath for your system

f = open(filepath+sys.argv[1], 'r+')

text = f.read()

f.close()

newtext = ''

for line in text.splitlines():
    newtext += line[::-1] + '\n'

#f.truncate(0)

fw = open(filepath+sys.argv[2], 'w')
fw.write(newtext)
fw.close()

print("Task complete!")





