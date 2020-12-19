import string

a = input("Please enter two strings: ")
b = input()

print("The letters that occur in both strings are: ", set(a) & set(b))
print("The letters that appear in a, but not in b are: ", set(a) - set(b), '\n')
print("The letters that appear in b, but not in a are: ", set(b) - set(a), '\n')
print("The letters that do not appear in either word are: ", set(string.ascii_lowercase) - set(a).union(set(b)), '\n')
