import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

result = a * b * c
number = [0 for _ in range(10)]

for i in str(result):
    number[int(i)] += 1

for j in number:
    print(j)