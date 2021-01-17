text1 = open("C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 8/Programming_Exercises/8.11/text1.txt", 'r').read()

bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

text1 = text1.lower()

for i in bad_chars:
    text1 = text1.replace(i, '')

s1 = set(text1.split())

x = set(input("Enter the word that you want to search for: "))

for word in s1:
    if x.issubset(set(word)):
        print(word)

