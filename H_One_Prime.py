x = int(input())
isPrime = True
for i in range(2, x):
    if x % i == 0:
        isPrime = False
        break
    else:
        isPrime = True


if isPrime == True:
    print("YES")
else:
    print("NO")