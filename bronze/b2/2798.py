import sys 
n, m = map(int, sys.stdin.readline().rstrip().split(" "))

numbers = list(map(int, sys.stdin.readline().rstrip().split(" ")))

max_value = 0

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            current = numbers[i] + numbers[j] + numbers[k]
            if current == m:
                max_value = current
                break
            elif current < m and current > max_value:
                max_value = current

print(max_value)