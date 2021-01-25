scores = open('results.txt', 'r').read()

l = []

print(scores)


res = [int(i) for i in scores.split()]          #converting to a list

for i in range(0, len(res) - 1, 2):             #converting to tuples
    l.append((res[i], res[i+1]))


frames = [0]

for i in range(10):
    if l[i][0] == 10 and l[i+1][0] == 10 and l[i+2][0] == 10:
        frames.append(30  + frames[-1])
        continue

    elif l[i][0] == 10 and l[i+1][0] == 10:
        frames.append(20 + l[i+2][0] + frames[-1])
        continue

    elif l[i][0] == 10:
        frames.append(10 + l[i+1][0] + l[i+1][1] + frames[-1])
        continue

    elif l[i][0] + l[i][1] == 10:
        frames.append(10 + l[i+1][0] + frames[-1])

    elif l[i][0] + l[i][1] < 10:
        frames.append(l[i][0] + l[i][1] + frames[-1])


print(frames)

print('Frame     Score')
print("-----     -----")


for i in range(1, len(frames)):
    print(' ', i,'      ', frames[i])

# 7 2    10 0    2 2    10 0    5 5    7 0    9 1    6 0    2 8    10 0    10 0   10 0
