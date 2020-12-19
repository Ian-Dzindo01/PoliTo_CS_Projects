a = int(input("Enter a prime numer n: " ))

l = [2,3]
for i in range(2, a):
    if i%2!=0 and i%3!=0:
        l.append(i)


print(l)

# NOTE: This is not the Sieve of Eratosthenes since you still have multiples of 5 remaining.
