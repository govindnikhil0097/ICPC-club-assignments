import sys
def func():
    for line in sys.stdin:
        pwd = line.strip()

        if not pwd:
            continue

        if pwd == "1999":
            print("Correct")
            break
        else:
            print("Wrong")


if __name__ == "__main__":
    func()