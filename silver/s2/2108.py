import sys

num = int(sys.stdin.readline().rstrip())
num_list = []
num_count_list = [[i, 0] for i in range(-4000, 4001)]

alive = []

for _ in range(num):
    n = int(sys.stdin.readline().rstrip())
    num_count_list[n+4000][1] += 1
    alive.append(n+4000)

max_count = 1
candidate = []

for i in range(-4000, 4001):
    if candidate:
        max_count = candidate[0][1]

    for j in range(num_count_list[i+4000][1]):
        num_list.append(i)    
        
    if num_count_list[i+4000][1] > max_count:
        candidate.clear()
        candidate.append(num_count_list[i+4000])

    elif num_count_list[i+4000][1] == max_count:
        candidate.append(num_count_list[i+4000])

m = round(sum(num_list)/len(num_list))

if len(candidate) >= 2:
    c = candidate[1][0]
else:
    c = candidate[0][0]

print("%.0f"%(m))
print(num_list[len(num_list)//2])
print(c)
print(max(num_list) - min(num_list))
