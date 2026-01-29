import sys

class Space:
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey

class Paper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.overlap_area = []

def overlap_space(p, q):
    ix0 = max(p.x, q.x)
    ix1 = min(p.x + 10, q.x + 10)
    iy0 = max(p.y, q.y)
    iy1 = min(p.y + 10, q.y + 10)

    if ix0 < ix1 and iy0 < iy1:
        overlap = Space(
            sx=ix0 - p.x,
            sy=iy0 - p.y,
            ex=ix1 - p.x - 1,  # inclusive
            ey=iy1 - p.y - 1   # inclusive
        )
        p.overlap_area.append(overlap)        

def calcul_space(p):
    color_paper = [[0]*10 for _ in range(10)]
    for o in p.overlap_area:
        for i in range(o.sx, o.ex+1):
            color_paper[i][o.sy:o.ey+1] = [1] * (o.ey - o.sy + 1)
    return sum(row.count(0) for row in color_paper)

num = int(str(sys.stdin.readline().rstrip()))
paper_list = []

for i in range(num):
    x, y = map(int, (sys.stdin.readline().rstrip().split()))
    p = Paper(x, y)
    paper_list.append(p)

    for op in paper_list:
        if p == op:
            continue
        overlap_space(p, op)

psum = 0
for p in paper_list:
    csum = calcul_space(p)
    psum = psum + csum

print(psum)