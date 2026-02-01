import sys

def is_VPS(plist):
    right_p = []
    while plist:
        p = plist.pop()
        if p == ')':
            right_p.append(1)
        else:
            if right_p:
                right_p.pop()
                continue
            else:
                return 0
    if right_p:
        return 0
    return 1


n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    p_list = [s for s in sys.stdin.readline().rstrip()]
    if is_VPS(p_list):
        print('YES')
    else:
        print('NO')