def countVowels(s1):
    cnt= 0
    for i in s1:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            cnt += 1

    return cnt


def countWords(s1):
    return len(s1.split())


def find1(s1, match):
   return True if s1 in match else False


def balance(yrs, bal, iRate):
    for i in range(yrs):
        bal -= bal*iRate

    return bal


def romanToDec(s1):

    total = 0

    d = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
    }

    for s in range(len(s1)):

        if s == len(s1) - 1:
            total += d[s1[s]]
            return total

        if d[s1[s]] < d[s1[s+1]]:
            total -= d[s1[s]]
        else:
            total += d[s1[s]]

    return total


