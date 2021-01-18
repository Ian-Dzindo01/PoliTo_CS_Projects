filepath = "C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 7/7.5/"  # change this filepath for your system

x = input("Please enter the name of the file to be read: ")

bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

text = open(filepath+x, 'r').read()

text = text.lower()

for i in bad_chars:
    text = text.replace(i, '')

print("The number of lines in the text is: ", len(text.splitlines()))
print("The number of words in the text is: ", len(text.split()))
print("The number of characters in the text is: ", sum([len(word) for word in text.split()]))
