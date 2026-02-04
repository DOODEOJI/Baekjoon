import sys

n = int(sys.stdin.readline().rstrip())
time_table = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split(" "))
    time_table.append([start, end])

time_table.sort(key=lambda x:[x[1],x[0]])

idx = 0
candidate = 1
cnt = 0

while (idx < len(time_table)):
    cnt += 1
    while (candidate < len(time_table)) and (time_table[idx][1] > time_table[candidate][0]):
        candidate += 1
    idx = candidate
    candidate += 1

print(cnt)

