import sys

n = int(sys.stdin.readline().rstrip())
current = 1

m = [[1, 1], [1, 0]]
result = [[1, 0], [0, 1]]

while current <= n:
    if n & current:
        temp1 = [[],[]]
        for i in range(2):
            for j in range(2):
                s = 0
                for k in range(2):
                    s += (m[i][k] * result[k][j])
                temp1[i].append(s%1000000007)
        result = temp1
    
    current <<= 1
    temp2 = [[],[]]
    for i in range(2):
        for j in range(2):
            s = 0
            for k in range(2):
                s += (m[i][k] * m[k][j])
            temp2[i].append(s%1000000007)
    m = temp2
    
print(result[0][1])