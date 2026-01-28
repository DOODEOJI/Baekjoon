import sys

num = int(str(sys.stdin.readline().rstrip()))
stack = []

for i in range(num):
    num = int(str(sys.stdin.readline().rstrip()))

    if num == 0 and stack:
        stack.pop()

    else:
        stack.append(num)

print(sum(stack))