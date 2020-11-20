lst = [1,3,4,12,14,20,22,15,17,28]

def avgList(lst):
    lst1 = []
    for i in range(len(lst)):
        if i == 0:
            lst1.append((lst[i] + lst[i+1])/2)

        elif i == (len(lst) - 1):
            lst1.append((lst[i] + lst[i-1])/2)

        else:
            lst1.append((lst[i-1] + lst[i] + lst[i+1])/3)

    return lst1

lst = avgList(lst)
print(lst)







