# Writing intersection, difference and union functions for a multiset

def union(s1, s2):
    s3 = {}
    for key in s1.keys():
        s3[key] = s1[key] + s2[key]

    return s3


def intersection(s1, s2):
    s3 = {}
    for key in s1.keys():
        s3[key] = s1[key] if s1[key] <= s2[key] else s2[key]

    return s3


def difference(s1, s2):
    s3 = {}
    for key in s1.keys():
        s3[key] = abs(s1[key] - s2[key])

    return s3



s1 = {'apples':6, 'oranges':12, 'bananas':18, 'mandarins':3}
s2 = {'apples':5, 'oranges':17, 'bananas':3, 'mandarins':8}

