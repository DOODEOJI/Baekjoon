import sys

n = int(sys.stdin.readline().rstrip())

is_yoon = False
if n%4 == 0:
    if n%400 ==0:
        is_yoon = True
        
    if n%100 !=0:
        is_yoon = True

if is_yoon:
    print("1") 
else:
    print("0")
