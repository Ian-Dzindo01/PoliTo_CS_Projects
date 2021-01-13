s1 = {1,'r',2,3,'h',7,10}
s2 = {5,'a',7,'n','a','i'}

s1 |= s2

for t in s1:
    if isinstance(t, str):
        print(t)
