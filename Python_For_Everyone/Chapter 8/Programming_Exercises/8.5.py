import sys

d = {}

while(True):
    a = input("\nPress p if you want to print the current list or s if you want to add a new student: "
              "\n\nPress t if you want to terminate the program: ")


    if a == 'p':
        if not d:
            print("There are not students on the list yet!")
            continue

        for i in list(d.keys()):
            print(i, ':', d[i])


    elif a == 's':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        d[name] = grade


    elif a == 't':
        sys.exit()






