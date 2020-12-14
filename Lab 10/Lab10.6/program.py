import sys
import string
import numpy as np


temp = sys.argv[2][2:]          #removes first two chars from str

temp = list("".join(dict.fromkeys(temp)))        #removes duplicates

alph = list(string.ascii_uppercase)
alph.remove('J')

i = 0
while(True):                                    # removing key letters from the alphabet
    if alph[i] in temp:
        del alph[i]
        i -= 1

    i += 1
    if i == len(alph)-1:
        break


keys = temp + alph

key_arr = []

for i in range(0,26,5):
    key_arr.append(keys[i:i+5])

key_arr.pop()
print(key_arr)

text = open(sys.argv[3], 'r').read()     # reading in the files

# if sys.argv[1] == '-e':
#     for i in range(0, len(text)-1, 2):
#         ind1 = key_arr.index(text[i])
#         ind2 = key_arr.index(text[i+1])

    # text = "".join([str(elem) for elem in s])







# if sys.argv[1] == '-d':


