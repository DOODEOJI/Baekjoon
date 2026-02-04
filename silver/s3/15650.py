import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

arr = []
visited = [False] * (N+1)

def backtracking():
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            if arr and arr[-1] > i:
                continue
            visited[i] = True
            arr.append(i)
            backtracking()
            arr.pop()
            if arr:
                visited[i] = False

backtracking()
