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


