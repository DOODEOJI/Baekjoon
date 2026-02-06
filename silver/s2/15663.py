import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
n_list = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

arr = []
seen = set()
ordered = []

visited = [False] * (N+1)

def backtracking():
    if len(arr) == M:
        t = tuple(arr)
        if t not in seen:
            seen.add(t)
            ordered.append(arr.copy())
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(n_list[i-1])
            backtracking()
            arr.pop()
            visited[i] = False

backtracking()
for i in ordered:
    print(*i)