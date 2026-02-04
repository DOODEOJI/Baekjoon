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
            visited[i] = True
            arr.append(i)
            backtracking()
            arr.pop()
            visited[i] = False

backtracking()
