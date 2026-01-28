import sys
num = int(str(sys.stdin.readline().rstrip()))

tsum = 0
cnt = 0

for i in range(1, num+1):
    tsum += i
    cnt += 1

    if tsum >= num:
        break

index = cnt - (tsum - num)
left_direction = True if cnt % 2 == 0 else False

if left_direction:
    for i in range(cnt):
        if (i+1) == index:
            print(str(i+1) + "/" + str(cnt-i))

else:
    index = cnt - index + 1
    for i in range(cnt):
        if (i+1) == index:
            print(str(i+1) + "/" + str(cnt-i))