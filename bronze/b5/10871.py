import sys

n, x = map(int, sys.stdin.readline().rstrip().split(" "))

numbers = list(map(int, sys.stdin.readline().rstrip().split(" ")))

for i in numbers:
    if i < x:
        print(i, end=" ")
