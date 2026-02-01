import sys
n = list(map(int, sys.stdin.readline().rstrip().split(" ")))

is_mixed = False

if n[0] == 1:
    for i in range(1, 9):
        if n[i-1] != i:
            is_mixed = True
            break
    if is_mixed:
        print("mixed")
    else:
        print("ascending")

elif n[0] == 8:
    for i in range(8, 0, -1):
        if n[-i+8] != i:
            is_mixed = True
            break
    if is_mixed:
        print("mixed")
    else:
        print("descending")

else:
    print("mixed")