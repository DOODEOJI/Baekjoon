import sys

# 처음 구현한 solution
n, tree_h = map(int, sys.stdin.readline().rstrip().split(" "))
tree_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
tree_list.sort(reverse = True)

cnt = 0
tsum = 0
idx = 0

for i in range(tree_list[0], -1, -1):
    tsum += cnt

    if tsum >= tree_h:
        break
    
    while (len(tree_list) - idx > 0):
        if i <= tree_list[idx]:
            cnt += 1
            idx += 1
        else:
            break

print(i)


# 이진 탐색 버전 solution

n, tree_h = map(int, sys.stdin.readline().rstrip().split(" "))
tree_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

def check(pivot):
    tsum = 0
    for i in tree_list:
        tsum += max(0, i - pivot)
    return tsum >= tree_h

i = 0
j = max(tree_list)
ans = 0

while (j >= i):
    mid = (i+j) // 2
    if check(mid):
        ans = mid
        i = mid + 1
    else:
        j = mid - 1
print(ans)