import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
matrix = []

for _ in range(n):
    m_list = list(sys.stdin.readline().rstrip())
    temp = []
    for i in range(m):
        temp.append(int(m_list[i]))
    matrix.append(temp)

process = deque([(0, 0, 0, 1)])
# 이전에 벽이 부서진 상태에서 visit 한건지 구분이 필요하므로
# 3차원으로 구성해야함
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

while True:
    if not process:
        print(-1)
        break
    p = process.popleft()

    if p[0] == n-1 and p[1] == m-1:
        print(p[3])
        break
    break_wall = p[2]
    
    if visited[p[0]][p[1]][break_wall]:
        continue
    visited[p[0]][p[1]][break_wall] = 1

    dist = p[3]

    if p[0] > 0 and not matrix[p[0]-1][p[1]]:
        process.append((p[0]-1, p[1], break_wall, dist + 1))

    elif p[0] > 0 and matrix[p[0]-1][p[1]] and not break_wall:
        process.append((p[0]-1, p[1], 1, dist + 1))

    if p[0] < n-1 and not matrix[p[0]+1][p[1]]:
        process.append((p[0]+1, p[1], break_wall, dist + 1))

    elif p[0] < n-1 and matrix[p[0]+1][p[1]] and not break_wall:
        process.append((p[0]+1, p[1], 1, dist + 1))

    if p[1] > 0 and not matrix[p[0]][p[1]-1]:
        process.append((p[0], p[1]-1, break_wall, dist + 1))

    elif p[1] > 0 and matrix[p[0]][p[1]-1] and not break_wall:
        process.append((p[0], p[1]-1, 1, dist + 1))

    if p[1] < m-1 and not matrix[p[0]][p[1]+1]:
        process.append((p[0], p[1]+1, break_wall, dist + 1))

    elif p[1] < m-1 and matrix[p[0]][p[1]+1] and not break_wall:
        process.append((p[0], p[1]+1, 1, dist + 1))


# 방향 벡터 사용 버전

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

process = deque([(0, 0, 0, 1)])
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

while True:
    if not process:
        print(-1)
        break

    x, y, wall, dist = process.popleft()

    if x == n-1 and y == m-1:
        print(dist)
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not matrix[nx][ny] and not visited[nx][ny][wall]:
                visited[nx][ny][wall] = 1
                process.append((nx, ny, wall, dist+1))

            if matrix[nx][ny] and not wall and not visited[nx][ny][wall]:
                visited[nx][ny][1] = 1
                process.append((nx, ny, 1, dist+1))
            

        
