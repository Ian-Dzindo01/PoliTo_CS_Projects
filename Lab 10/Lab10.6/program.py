import sys
import string

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
print(keys)


# if sys.argv[1] == '-d':


# if sys.argv[1] == '-e':

