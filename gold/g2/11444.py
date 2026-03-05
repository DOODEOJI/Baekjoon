import sys

n = int(sys.stdin.readline().rstrip())

m1 = [[1, 1], [1, 0]]
m2 = [[1, 1], [1, 0]]

for _ in range(n-1):
    temp = [[],[]]
    for i in range(2):
        for j in range(2):
            s = 0
            for k in range(2):
                s += (m2[i][k] * m1[k][j])
            temp[j].append(s%1000000007)
    m2 = temp

print(m2[0][1])