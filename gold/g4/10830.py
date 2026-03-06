import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
current = 1

matrix = []
for _ in range(n):
    sub = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    matrix.append(sub)

# 항등행렬로 시작
result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

while current <= m:
    if m & current:
        temp1 = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                s = 0
                for k in range(n):
                    s += (matrix[i][k] * result[k][j])
                temp1[i].append(s%1000)
        result = temp1
    
    current <<= 1
    temp2 = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += (matrix[i][k] * matrix[k][j])
            temp2[i].append(s%1000)
    matrix = temp2
    
for r in result:
    print(*r)