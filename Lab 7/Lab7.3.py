def equals(a, b):
    for i in range(len(a)):
        if  a[i] != b[i]:
            print("The two lists are not equal!")
            return 0

    print("The two lists are equal!")

a = [1,2,3,4,5]
b = [1,2,3,4,6]

equals(a, b)
