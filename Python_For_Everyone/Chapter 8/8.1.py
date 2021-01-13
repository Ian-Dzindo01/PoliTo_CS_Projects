s1 = {1,2,3}
s2 = {1,2,3,4,5,6}

def isTrueSubset(s1, s2):
    if s1 == s2:
        return False

    if s1.issubset(s2):
        return True


print(isTrueSubset(s1, s2))

