import sys
import math

n = int(sys.stdin.readline().rstrip())
t_shirt = list(map(int, sys.stdin.readline().rstrip().split(" ")))
t, p = map(int, sys.stdin.readline().rstrip().split(" "))

t_num = 0
for s in t_shirt:
    t_num += math.ceil((s / t))

print(t_num)
print(n // p, n % p)