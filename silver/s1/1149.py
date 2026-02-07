import sys

n = int(sys.stdin.readline().rstrip())
house = [[0,0,0]]

for _ in range(n):
    rgb = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    house.append(rgb)

for i in range(1, n+1):
    result = []
    for j in range(3):
        temp = house[i-1].copy()
        temp.pop(j)
        house[i][j] += min(temp)
    
print(min(house[-1]))