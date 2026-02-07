import sys 

# 밟은 계단 마킹
T = int(sys.stdin.readline().rstrip())
stairs = []

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    stairs.append(n)

dp = [[0,0],[stairs[0], stairs[0]]]

for i in range(2, T+1):
    dp0 = max(dp[i-2][0], dp[i-2][1]) + stairs[i-1]
    dp1 = dp[i-1][0] + stairs[i-1]
    dp.append([dp0, dp1])

print(max(dp[T]))

# 밟지 않은 계단 마킹
# 밟지 않는 경우의 수는 이전 계단을 밟고 두 칸 건너 뛰는 경우밖에 없음

stairs.append(0) # 마지막은 무조건 밟아야하므로 마지막 다음 걸 건너뛰게
dp = [0, stairs[0], stairs[1]]

for i in range(3, T+2):
    dp.append(min(dp[i-2], dp[i-3]) + stairs[i-1])

print(sum(stairs) - dp[T+1])