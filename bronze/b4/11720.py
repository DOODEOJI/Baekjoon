import sys
n = int(sys.stdin.readline().rstrip())

num = sys.stdin.readline().rstrip()

sum = 0
for n in num:
    sum += int(n)

print(sum)