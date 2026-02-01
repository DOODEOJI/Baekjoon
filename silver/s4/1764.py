import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

unknown = set()
unseen = set()

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    unknown.add(name)

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    unseen.add(name)

final = unknown & unseen

print(len(final))
if len(final):
    final = sorted(list(final))
    for i in final:
        print(i)