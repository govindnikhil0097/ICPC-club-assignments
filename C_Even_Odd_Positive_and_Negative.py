import sys

def func():
    n = int(input())
    num = list(map(int, input().split()))

    even, pos, odd, neg = 0, 0, 0, 0

    for i in num:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

        if i > 0:
            pos += 1
        elif i < 0:
            neg +=1 

    print(f"Even: {even}")
    print(f"Odd: {odd}")
    print(f"Positive: {pos}")
    print(f"Negative: {neg}")

if __name__ == "__main__":
    func()