import sys

def func():
    w = int(input())

    if w == 1:
        print(-1)
    for i in range(2, w+1, 2):
        print(i)

if __name__ == "__main__":
    func()