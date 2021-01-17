# count the occurrence of each word in a text,
# while also using a cache to avoid repeating the same procces for same files

from collections import Counter

cache = {}

filepath = 'C:/Users/iandz/OneDrive/Desktop/Faks/CS/Lab/Python_For_Everyone/Chapter 8/Programming_Exercises/8.19/' # your filepath

while(True):
    x = input("Please enter the file name or just enter t if you want to exit: ")
    print('\n')

    if x == 't':
        break

    if x in cache:
        print("Data retrieved from cache. \n")
        print(cache[x])
        print('\n')
        continue

    text = open(filepath+x, 'r').read()

    bad_chars = [';', ':', '!', "*", "'", '.', ',', '!', '?', '"', '(', ')']

    text = text.lower()

    for i in bad_chars:
        text = text.replace(i, '')

    d1 = Counter(text.split())

    print(d1,'\n')

    cache[x] = d1


print("You have successfuly terminated the program, see you next time!")

