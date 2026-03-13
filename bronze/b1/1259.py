import sys

while True:
    num = sys.stdin.readline().rstrip()
    if num == "0":
        break
    i = 0
    j = len(num) - 1

    found = True
    while i < j:
        if num[i] != num[j]:
            found = False
            break
        i += 1
        j -= 1

    if found:
        print("yes")
    else:
        print("no")