filepath = "C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 7/7.8/"     # you will need to change this filepath for your system

x = input("Please enter the name of the file whose contents you want reversed: ")

f = open(filepath+x, 'r+')

text = f.read()

f.close()

newtext = ''

for line in text.splitlines():
    newtext += line[::-1] + '\n'

#f.truncate(0)

fw = open(filepath+'text.txt', 'w')
fw.write(newtext)
fw.close()






