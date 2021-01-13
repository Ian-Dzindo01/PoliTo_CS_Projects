s1 = {1,'r',2,3,'h',7,10,'i'}
s2 = {5,'a',7,'n','a','i'}

s3 = s1 - s2

for t in s3:
    if isinstance(t, str):
        print(t)
