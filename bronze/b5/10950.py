import sys

k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    print(a+b)