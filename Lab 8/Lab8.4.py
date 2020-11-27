def mergeSorted(a, b):
    lst = []
    aind = 0
    bind = 0

    lna = len(a)
    lnb = len(b)

    while(aind != lna and bind != lnb):
        if min(a) > min(b):
            lst.append(min(b))
            b.remove(min(b))
            bind += 1

        elif min(a) < min(b):
            lst.append(min(a))
            a.remove(min(a))
            aind += 1

        else:
            lst.append(min(a))
            a.remove(min(a))

            lst.append(min(b))
            b.remove(min(b))

            bind += 1
            aind += 1

        if not a:
            lst.append(b[0])

        if not b:
            lst.append(a[0])

    return lst

a = [10,33,35,78,123]
b = [22,33,34,35,36,99]

res = mergeSorted(a,b)

print(res)










