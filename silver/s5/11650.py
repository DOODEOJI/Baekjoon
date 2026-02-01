import sys

n = int(sys.stdin.readline().rstrip())
track = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    track.append([x, y])

track.sort(key=lambda x:(x[0],x[1]))

for i in track:
    print(i[0], i[1])