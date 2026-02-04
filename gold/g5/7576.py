import sys

class Box:
    def __init__(self, value):
        self.value = value
        self.top = None
        self.btm = None
        self.right = None
        self.left = None
        self.visited = False
    def __repr__(self):
        return f"{self.value}"

process = []

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
b_list = [[Box(i) for i in map(int, sys.stdin.readline().rstrip().split(" "))] for _ in range(m)]
current = []

for i in range(m):
    for j in range(n):
        if b_list[i][j].value == 1:
            current.append(b_list[i][j])
        if (i-1)>=0:
            b_list[i][j].top = b_list[i-1][j]

        if (i+1)<m:
            b_list[i][j].btm = b_list[i+1][j]

        if (j-1)>=0:
            b_list[i][j].left = b_list[i][j-1]

        if (j+1)<n:
            b_list[i][j].right = b_list[i][j+1]

switch = False
next = []
day = -1

while True:
    if not current and not next:
        break
    
    if switch:
        while (next):
            ne = next.pop()
            if ne.visited:
                continue
            ne.visited = True
            if ne.top and not ne.top.visited and ne.top.value == 0:
                ne.top.value = 1
                current.append(ne.top)

            if ne.btm and not ne.btm.visited and ne.btm.value == 0:
                ne.btm.value = 1
                current.append(ne.btm)

            if ne.left and not ne.left.visited and ne.left.value == 0:
                ne.left.value = 1
                current.append(ne.left)

            if ne.right and not ne.right.visited and ne.right.value == 0:
                ne.right.value = 1
                current.append(ne.right)

        day += 1
        switch = False

    else:
        while (current):
            c = current.pop()
            if c.visited:
                continue
            c.visited = True
            if c.top and not c.top.visited and c.top.value == 0:
                c.top.value = 1
                next.append(c.top)

            if c.btm and not c.btm.visited and c.btm.value == 0:
                c.btm.value = 1
                next.append(c.btm)

            if c.left and not c.left.visited and c.left.value == 0:
                c.left.value = 1
                next.append(c.left)

            if c.right and not c.right.visited and c.right.value == 0:
                c.right.value = 1
                next.append(c.right)

        day += 1
        switch = True

for i in range(m):
    for j in range(n):
      if b_list[i][j].value == 0:
        day = -1

print(day)