def swapFandL(a):
    f = a[0]
    l = a[len(a)-1]

    a[0] = l
    a[len(a)-1] = f

    return a


def shiftOne(a):
    a.insert(0, a.pop())
    return a


def replaceWith0(a):
    for i in range(len(a)):
        if a[i]%2 == 0:
            a[i] = 0


    return a


def replaceNeighbour(a):
    newL = []
    newL.append(a[0])
    for i in range(1, len(a)-1):
        newL.append(a[i-1] if a[i-1] > a[i+1] else a[i+1])

    newL.append(a[len(a)-1])
    return newL


def removeMiddle(a):
    if len(a)%2 == 0:
        a.pop(len(a)//2)
        a.pop((len(a)//2))
    else:
        a.pop(len(a)//2)

    return a


def returnSecLargest(a):
    a.sort(reverse=True)
    return a[1]


def sortedList(a):
    for i in range(1, len(a)):
        if a[i-1] >= a[i]:
            return False

    return True


def adjDupl(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return True

    return False


def adjEl(a):
    if len(a) != len(set(a)):
        return True

    return False














