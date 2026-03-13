import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

if a > b:
    x = a
    y = b

else:
    x = b
    y = a

remain = 1

while remain:
    remain = x % y
    x = y
    y = remain

print(x)
print(int((a/x * b/x)*x))
