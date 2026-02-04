import sys

n, fi, fj = map(int, sys.stdin.readline().rstrip().split(" "))

# 재귀 버전 (시간초과)
n_list = [
    [0 for _ in range(2 ** n)] for _ in range(2 ** n)
]

found = False

def four_basic(row_start, row_end, column_start, column_end):
    global cnt, found
    if found:
        return
    if (row_end - row_start) < 2:
        return
    
    elif (row_end - row_start) == 2:
        for i in range(2):
            for j in range(2):
                n_list[row_start+i][column_start+j] += cnt
                if (row_start + i) == fi and (column_start + j) == fj:
                    found = True
                    return
                cnt += 1
        return
    
    else:
        four_basic(row_start, (row_start+row_end)//2, column_start, (column_start+column_end)//2)
        four_basic(row_start, (row_start+row_end)//2, (column_start+column_end)//2, column_end)
        four_basic((row_start+row_end)//2, row_end, column_start, (column_start+column_end)//2)
        four_basic((row_start+row_end)//2, row_end, (column_start+column_end)//2, column_end)

cnt = 0
four_basic(0, 2 ** n, 0, 2 ** n)
print(cnt)

# 규칙으로 풀이 (4진수 기반 자리 붙이기)

track = []
row_start = 0
row_end = 2 ** n
column_start = 0
column_end = 2 ** n

ans = 0

while n > 0:
    if row_start <= fi < (row_start+row_end)//2 and column_start <= fj < (column_start+column_end)//2:
        ans = ans * 4 + 0
        row_end = (row_start+row_end)//2
        column_end = (column_start+column_end)//2

    elif row_start <= fi < (row_start+row_end)//2 and (column_start+column_end)//2 <= fj < column_end:
        ans = ans * 4 + 1
        row_end = (row_start+row_end)//2
        column_start = (column_start+column_end)//2

    elif (row_start+row_end)//2 <= fi < row_end and column_start <= fj < (column_start+column_end)//2:
        ans = ans * 4 + 2
        row_start = (row_start+row_end)//2
        column_end = (column_start+column_end)//2

    elif (row_start+row_end)//2 <= fi < row_end and (column_start+column_end)//2 <= fj < column_end:
        ans = ans * 4 + 3
        row_start = (row_start+row_end)//2
        column_start = (column_start+column_end)//2
    n -= 1

print(ans)