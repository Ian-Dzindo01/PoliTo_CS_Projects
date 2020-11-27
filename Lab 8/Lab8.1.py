l1 = [1,3,5,7,9,11]
l2 = [2,4,6]

def merge(a,b):
    l = []
    cnt = len(a) if len(a) > len(b) else len(b)

    for i in range(cnt):

        if i < len(a):
            l.append(a[i])

        if i < len(b):
            l.append(b[i])

    return l

l = merge(l1,l2)
print(l)


