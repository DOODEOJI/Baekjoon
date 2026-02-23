import sys

class Node:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None

def pre_traversal(p):
    if p.root == None:
        return
    
    result.append(p.root)

    if p.left:
        pre_traversal(p.left)

    if p.right:
        pre_traversal(p.right)

def in_traversal(p):
    if p.root == None:
        return
    
    if p.left:
        in_traversal(p.left)

    result.append(p.root)

    if p.right:
        in_traversal(p.right)

def post_traversal(p):
    if p.root == None:
        return
    
    if p.left:
        post_traversal(p.left)

    if p.right:
        post_traversal(p.right)

    result.append(p.root)

n = int(sys.stdin.readline().rstrip())
prev = []
result = []

for i in range(n):
    ro, le, ri = map(str, sys.stdin.readline().rstrip().split(" "))
    
    if le == ".":
        le = None
    if ri == ".":
        ri = None

    if prev:
        idx = 0
        for p in prev:
            if p.root == ro:
                idx = prev.index(p)
                
        current = prev.pop(idx)
        current.left = Node(le)
        current.right = Node(ri)
        prev.extend([current.left, current.right])

    if i == 0:
        root = Node(ro)
        root.left = Node(le)
        root.right = Node(ri)
        prev.extend([root.left, root.right])
    
pre_traversal(root)
in_traversal(root)
post_traversal(root)

cnt = 0
for w in result:
    if cnt == n-1:
        print(w)
        cnt = 0
        continue

    print(w, end='')
    cnt += 1