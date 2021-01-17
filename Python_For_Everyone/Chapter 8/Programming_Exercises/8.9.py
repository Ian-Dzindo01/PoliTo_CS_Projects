import string

s1 = set(input("Enter the first string: "))
s2 = set(input("Enter the second string: "))

print("These are the letters that occur in both strings: ", list(s1&s2), '\n')
print("These are the letters that appear in the first string, but not in the second: ", s1-s2, '\n')
print("These are the letters that appear in the first string, but not in the second: ", s2-s1, '\n')

s1 |= s2
print("These are the letters that don't appear in either string: ", set(string.ascii_lowercase)-s1)
