import sys

hour, minute = map(int, sys.stdin.readline().rstrip().split(" "))

if minute < 45:
    minute = 60 - (45 - minute)
    hour -= 1
    if hour == -1:
        hour = 23
    if minute == 60:
        minute = "00"

else:
    minute = minute - 45

print(hour, minute)