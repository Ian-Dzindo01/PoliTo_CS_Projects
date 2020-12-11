fr = open('classes.txt', 'r')
text = fr.read()
classes = []

for line in text.splitlines():
    classes.append(line)

studentid = input("Please enter a student ID: ").strip()
s = 'STUDENT ID ' + studentid + '\n'

for c in classes:
    with open('C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Lab 10/Lab10.7/Test Results/' + c + '.txt') as f:
        text = f.read()
        for line in text.splitlines():
            if studentid in line:
                s += c + ' ' + line[-2:].strip() + '\n'


print(s)







