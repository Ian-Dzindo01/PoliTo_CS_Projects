def sparseArraySum(d1,d2):
    l = []

    largestd1 = list(d1.keys())[len(d1.keys())-1]
    largestd2 = list(d2.keys())[len(d2.keys())-1]

    if largestd1 > largestd2:
        largest = largestd1+1
    else:
        largest = largestd2+1

    for i in range(largest):
        l.append(0)
        if i in d1:
            l[i] += d1[i]

        if i in d2:
            l[i] += d2[i]


    return l


d1 = {1:2, 3:12, 5:18, 6:17}
d2 = {1:3, 2:4, 5:2, 11:1}

c = sparseArraySum(d1, d2)

print(c)
