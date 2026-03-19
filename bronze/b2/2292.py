import sys

n = int(sys.stdin.readline().rstrip())
bsum = 1
p = 1

while (bsum < n):
    bsum += (6 * p)
    p += 1

print(p)