import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    column = int(sys.stdin.readline().rstrip())
    sticker = []
    for i in range(2):
        l = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        sticker.append(l)

    process = [[0, sticker[0][0], sticker[1][0]]]

    for j in range(1, column):
        idx0 = max(process[j-1]) # 아무것도 선택 안함
        idx1 = sticker[0][j] + max([process[j-1][0], process[j-1][2]]) # 윗 열 선택
        idx2 = sticker[1][j] + max([process[j-1][0], process[j-1][1]]) # 아래 열 선택

        process.append([idx0, idx1, idx2])

    print(max(process[-1]))