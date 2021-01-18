filepath = "C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 7/7.4/"   # change this filepath for your system

filename = input("Please enter the file name to be read in: ")

text = open(filepath+filename, 'r').read()

res1 = []
res2 = []

s = "66.4, 19.8"

print(s.split(',')[0])

for line in text.splitlines():
    res1.append(float(line.split(',')[0]))
    res2.append(float(line.split(',')[1]))

print("The average of the first list is: ", sum(res1)/(len(res1)))
print("The average of the second list is: ", sum(res2)/len(res2))






