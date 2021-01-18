import sys

word = sys.argv[1]

files = list(sys.argv)[2:]

for file in files:
    with open(file, 'r') as f:
        text = f.read()
        for line in text.splitlines():
            if word in line:
                print(file,': ', line, '\n')



# run the program from the command line with the following command (you might have to change the names of some files in the command for your system)

# python find.py benz text1.txt text2.txt text3.txt text4.txt text5.txt text6.txt



