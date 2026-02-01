import sys

n = int(sys.stdin.readline().rstrip())

t = list(map(int, sys.stdin.readline().rstrip().split(" ")))
t.sort()

sum = 0
while(n > 0):
    for i in range(0, n):
        sum += t[i]
    n -= 1

print(sum)