import sys

n = int(sys.stdin.readline().rstrip())
found = False

for i in range(n):
    nsum = 0
    for j in str(i):
        nsum += int(j)
    nsum += i

    if nsum == n:
        found = True
        print(i)
        break

if not found:
    print(0)