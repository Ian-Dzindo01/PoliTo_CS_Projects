s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

common = list(set(s1)&set(s2))

print(common)