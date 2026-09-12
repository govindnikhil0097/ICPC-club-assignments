x = int(input())
isPrime = True
l = []
for i in range(2, x+1):
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
        else:
            isPrime = True
    if isPrime:
        l.append(i)

print(" ".join(map(str, l)))