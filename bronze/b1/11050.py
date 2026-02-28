import sys
import math

n, k = map(int, sys.stdin.readline().rstrip().split(" "))

print(int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))
