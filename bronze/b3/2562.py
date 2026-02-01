import sys

max_value = 0
idx = 0
for i in range(9):
    n = int(sys.stdin.readline().rstrip())
    if max_value < n:
        max_value = n
        idx = i

print(max_value)
print(idx+1)