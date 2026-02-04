import sys

class Tree:
    def __init__(self, value):
        self.root = value
        self.level = None
        self.one = None
        self.mone = None
        self.two = None
        
n, k = map(int, sys.stdin.readline().rstrip().split())
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

    if p.root == k:
        print(p.level)
        break

    if p.root - 1 >= 0:
        p.mone = Tree(p.root - 1)
        p.mone.level = p.level + 1
        process_list.append(p.mone)
    
    if p.root < 2 * k:

        if p.root + 1 <= 100000:
            p.one = Tree(p.root + 1)
            p.one.level = p.level + 1
            process_list.append(p.one)
    

        if p.root * 2 <= 100000:
            p.two = Tree(p.root * 2)
            p.two.level = p.level + 1
            process_list.append(p.two)