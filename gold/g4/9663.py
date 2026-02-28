import sys

n = int(sys.stdin.readline().rstrip())

col = [False for _ in range(n)]
diagl = [False for _ in range(2*n)]
diagr = [False for _ in range(2*n)]
count = 0

def n_queen(row):
    global count
    if row == n:
        count += 1

    for c in range(n):
        if col[c] or diagl[row+c] or diagr[row-c+n]:
            continue
        else:
            col[c] = True
            diagl[row+c] = True
            diagr[row-c+n] = True
            n_queen(row+1)
            col[c] = False
            diagl[row+c] = False
            diagr[row-c+n] = False
    return

n_queen(0)
print(count)   