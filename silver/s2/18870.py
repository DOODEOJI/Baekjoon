import sys

num = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
compare = sorted(set(n_list))

final = []

def check(n, pivot):
    return compare[pivot] >= n

for n in n_list:
    lo = 0
    hi = len(compare) - 1
    ans = 0

    while(lo <= hi):
        mid = (lo + hi) // 2
        if check(n, mid):
            ans = mid
            hi = mid - 1 
        else:
            lo = mid + 1
    final.append(ans)

print(*final)