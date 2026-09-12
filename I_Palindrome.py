x = int(input())
num = str(x)
y = ""
revNum = num[::-1]
if num == revNum:
    print(int(revNum))
    print("YES")
else:
    print(int(revNum))
    print("NO")
