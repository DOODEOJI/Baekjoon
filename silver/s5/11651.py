import sys

n = int(sys.stdin.readline().rstrip())
co = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    co.append((x,y))

co.sort(key = lambda x : [x[1], x[0]], reverse = False)

for i, j in co:
    print(i, j)