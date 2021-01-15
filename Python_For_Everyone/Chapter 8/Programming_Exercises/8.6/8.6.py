text = open("program.py", 'r').read()

indx = []

word = input("Please enter the word that you want found: ")

for cnt, line in enumerate(text.splitlines()):
    if word in line:
        indx.append(cnt+1)


print("\nThe word ", word, " is found in the following lines: ", indx)


