import sys

p = set()
for _ in range(10):
    n = int(sys.stdin.readline().rstrip())
    p.add(n%42)

print(len(p))