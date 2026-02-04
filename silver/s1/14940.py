import sys

class Unit:
    def __init__(self, value):
        self.value = value
        self.top = None
        self.btm = None
        self.right = None
        self.left = None
        self.level = 0
        self.visited = False
    
    def __repr__(self):
        return f"{self.level}"

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

unit_map = [
    [Unit(v) for v in map(int, sys.stdin.readline().rstrip().split())]
    for _ in range(n)
]

target = None

for i in range(n):
    for j in range(m):
        if not target:
            if unit_map[i][j].value == 2:
                target = (i, j)
        if (i-1)>=0:
            unit_map[i][j].top = unit_map[i-1][j]

        if (i+1)<n:
            unit_map[i][j].btm = unit_map[i+1][j]

        if (j-1)>=0:
            unit_map[i][j].left = unit_map[i][j-1]

        if (j+1)<m:
            unit_map[i][j].right = unit_map[i][j+1]

process = [unit_map[target[0]][target[1]]]

while process:
    p = process.pop(0)

    if p.visited:
        continue

    p.visited = True

    if p.top and not p.top.visited:
        if p.top.value:
            p.top.level = p.level + 1
            process.append(p.top)

        else:
            p.top.level = 0

    if p.btm and not p.btm.visited:
        if p.btm.value:
            p.btm.level = p.level + 1
            process.append(p.btm)

        else:
            p.btm.level = 0

    if p.right and not p.right.visited:
        if p.right.value:
            p.right.level = p.level + 1
            process.append(p.right)

        else:
            p.right.level = 0

    if p.left and not p.left.visited:
        if p.left.value:
            p.left.level = p.level + 1
            process.append(p.left)

        else:
            p.left.level = 0

for i in range(n):
    for j in range(m):
        if not unit_map[i][j].visited and unit_map[i][j].value:
            unit_map[i][j].level = -1

for m in unit_map:
    print(*m)