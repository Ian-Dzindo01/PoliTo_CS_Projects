# 5. What is the output of the following code snippet?

s = set()
for i in range(0, 20, 2) :
    s.add(i)
for i in range(0, 20, 3) :
    s.discard(i)

print(s)
