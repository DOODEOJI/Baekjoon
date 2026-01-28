import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [sys.stdin.readline().strip() for _ in range(N)]

def find_cnt_W(eN, eM, i_start, j_start):
    color_cnt = 0
    w_cnt = 1

    for i in range(i_start, eN):
        is_w = True if w_cnt % 2 == 1 else False

        if is_w and board[i][j_start] == 'B':
            color_cnt += 1
        
        if not is_w and board[i][j_start] == 'W':
            color_cnt += 1

        if (i-1) >= i_start:
            old_w = True if w_cnt % 2 == 0 else False
        
            if is_w and old_w:
                    color_cnt += 1
                    is_w = False
            elif not is_w and not old_w:
                    color_cnt += 1
                    is_w = True
        
        for j in range(j_start+1, eM):
            if is_w and board[i][j] == 'B':
                is_w = False

            elif is_w and board[i][j] == 'W':
                color_cnt += 1
                is_w = False
            
            elif not is_w and board[i][j] == 'B':
                color_cnt += 1
                is_w = True

            elif not is_w and board[i][j] == 'W':
                is_w = True

        w_cnt += 1

    return color_cnt

def find_cnt_B(eN, eM, i_start, j_start):
    color_cnt = 0
    b_cnt = 1

    for i in range(i_start, eN):
        is_b = True if b_cnt % 2 == 1 else False

        if is_b and board[i][j_start] == 'W':
            color_cnt += 1
        
        if not is_b and board[i][j_start] == 'B':
            color_cnt += 1

        if (i-1) >= i_start:
            old_b = True if b_cnt % 2 == 0 else False
        
        if is_b and (i-1) >= i_start:
            if old_b:
                color_cnt += 1
                is_b = False

        elif not is_b and (i-1) >= i_start:
            if not old_b:
                color_cnt += 1
                is_b = True

        for j in range(j_start+1, eM):
            if is_b and board[i][j] == 'B':
                color_cnt += 1
                is_b = False

            elif is_b and board[i][j] == 'W':
                is_b = False
            
            elif not is_b and board[i][j] == 'B':
                is_b = True

            elif not is_b and board[i][j] == 'W':
                color_cnt += 1
                is_b = True
        b_cnt += 1

    return color_cnt

min_cnt = 10000000
count = 0

for i in range(N-8+1):
    for j in range(M-8+1):
        cnt_w = find_cnt_W(i+8, j+8, i, j)
        cnt_b = find_cnt_B(i+8, j+8, i, j)

        min_wb = cnt_w if cnt_w < cnt_b else cnt_b
        if min_wb < min_cnt:
            min_cnt = min_wb

print(min_cnt)