import sys
import string

temp = sys.argv[2][2:]          #removes first two chars from str

temp = list("".join(dict.fromkeys(temp)))        #removes duplicates

alph = list(string.ascii_uppercase[::-1])

i = 0
while(True):                                    # removing key letters from the alphabet
    if alph[i] in temp:
        del alph[i]
        i -= 1

    i += 1
    if i == len(alph)-1:
        break

temp = ''.join([str(elem) for elem in temp])        # creating the key
alph = ''.join([str(elem) for elem in alph])
keys = temp + alph[:-1]

zip_iterator = zip(list(string.ascii_uppercase), list(keys))                # making the dictionary to be used in encrypting
d = dict(zip_iterator)

rev_zip_iterator = zip(list(keys), list(string.ascii_uppercase))            # the dictionary for decrypting
revd = dict(rev_zip_iterator)

fr = open(sys.argv[3], 'r')
text = (fr.read()).strip()                      # the .strip() is necessary in order to remove newline characters from the string

if sys.argv[1] == '-d':
    res = ''.join([str(revd[letter]) for letter in text])
    fw = open(sys.argv[4], 'w')
    text += '\n' + res
    fw.write(text)
    fw.close()

if sys.argv[1] == '-e':
    res = ''.join([str(d[letter]) for letter in text])
    fw = open(sys.argv[4], 'w')
    text += '\n' + res
    fw.write(text)
    fw.close()

