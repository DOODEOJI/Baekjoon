import sys

r = 31
m = 1234567891

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

hash_value = 0
idx = 0

for i in s:
    v = ord(i) - 96
    hash_value += (v * (r ** idx))
    idx += 1

print(hash_value % m)