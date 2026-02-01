import sys

class Tree:
    def __init__(self, value):
        self.root = value
        self.level = None
        self.one = None
        self.two = None
        self.three = None
        
n = int(sys.stdin.readline().rstrip())
t= Tree(n)

process_list = []
process_list.append(t)
t.level = 0
visited = []

while process_list:
    p = process_list.pop(0)
    if p.root in visited:
        continue
    visited.append(p.root)
    if p.root == 1:
        print(p.level)
        break

    if p.root % 2 == 0:
        p.two = Tree(p.root / 2)
        p.two.level = p.level + 1
        process_list.append(p.two)
    
    if p.root % 3 == 0:
        p.three = Tree(p.root / 3)
        p.three.level = p.level + 1
        process_list.append(p.three)

    p.one = Tree(p.root - 1)
    p.one.level = p.level + 1
    process_list.append(p.one)