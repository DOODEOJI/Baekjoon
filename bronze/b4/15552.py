import sys

it = int(str(sys.stdin.readline().rstrip('\n')))

for i in range(it):
    a, b = map(int, sys.stdin.readline().rstrip('\n').split(' '))
    print(a+b)