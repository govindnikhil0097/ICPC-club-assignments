import sys
def func():
    l = sys.stdin.read().split()
    n1 = int(l[0])
    n2 = int(l[1])
    commonDivsors = []

    if n1> n2:
        for i in range(1, n2 + 1):
            if n1 % i == 0 and n2 % i == 0:
                commonDivsors.append(i)
    else:
        for i in range(1, n1 + 1):
            if n1 % i == 0 and n2 % i == 0:
                commonDivsors.append(i)

    commonDivsors.sort(reverse=True)
    print(commonDivsors[0])
    
if __name__ == "__main__":
    func()