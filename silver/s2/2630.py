import sys

class Paper:
    def __init__(self, v):
        self.v = v

num = int(sys.stdin.readline().rstrip())
p_list = [list(map(str, sys.stdin.readline().rstrip().split(" "))) for _ in range(num)]
p_dict = {
    '0' : 0,
    '1' : 0
}

def check_change(p, sr, er, sc, ec):
    change = False
    current = p[sr][sc]

    if (er-sr) == 0:
        p_dict[current] += 1
        return
    
    for i in range(sr, er+1):
        for j in range(sc, ec+1):
            if p[i][j] != current:
                change = True
                break

    if change:
        check_change(p, sr, (sr+er)//2, sc, (sc+ec)//2)
        check_change(p, (sr+er)//2+1, er, sc, (sc+ec)//2)
        check_change(p, sr, (sr+er)//2, (sc+ec)//2+1, ec)
        check_change(p, (sr+er)//2+1, er, (sc+ec)//2+1, ec)

    else:
        p_dict[current] += 1
        return
    
check_change(p_list, 0, num-1, 0, num-1)
print(p_dict['0'])
print(p_dict['1'])