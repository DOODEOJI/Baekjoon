import sys

class Ground:
    def __init__(self, value):
        self.value = value
        self.top = None
        self.btm = None
        self.right = None
        self.left = None
    def __repr__(self):
        return f"{self.value}"

num = int(sys.stdin.readline().rstrip())
process = []

for _ in range(num):
    n, m , k = map(int, sys.stdin.readline().rstrip().split(" "))
    z_list = [[Ground(0) for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        i, j = map(int, sys.stdin.readline().rstrip().split(" "))
        (z_list[j][i]).value = 1
        if (j-1)>=0:
            z_list[j][i].top = z_list[j-1][i]

        if (j+1)<m:
            z_list[j][i].btm = z_list[j+1][i]

        if (i-1)>=0:
            z_list[j][i].left = z_list[j][i-1]

        if (i+1)<n:
            z_list[j][i].right = z_list[j][i+1]

        process.append(z_list[j][i])

    sprocess = []
    cnt = 0
    while process:
        p = process.pop()
        cnt += 1
        
        if p.value == -1:
            cnt -= 1
            continue
        
        p.value = -1
        sprocess.append(p)

        while sprocess:
            s = sprocess.pop()
            s.value = -1

            if s.top and s.top.value == 1:
                s.top.value = -1
                sprocess.append(s.top)
            if s.btm and s.btm.value == 1:
                s.btm.value = -1
                sprocess.append(s.btm)
            if s.right and s.right.value == 1:
                s.right.value = -1
                sprocess.append(s.right)
            if s.left and s.left.value == 1:
                s.left.value = -1
                sprocess.append(s.left)

    print(cnt)