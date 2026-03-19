import sys

result = 0
for i in range(3):
    n = sys.stdin.readline().rstrip()
    if n.isdigit():
        result = int(n) + 3 - i
        break

if not result % 3 and not result % 5:
    print("FizzBuzz")
elif not result % 3:
    print("Fizz")
elif not result % 5:
    print("Buzz")
else:
    print(result)