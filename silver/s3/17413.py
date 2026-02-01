import sys

string = sys.stdin.readline().rstrip()

def back_flip(s):
    new_s = ''
    i = len(s)-1
    while(i >= 0):
        new_s += s[i]
        i -= 1
    return new_s

final_str = ''
temp = ''

i = 0
while(i < len(string)):
    if string[i] == "<":
        if temp:
            final_str += back_flip(temp)
            temp = ''
        while True:
            if string[i] == ">":
                break
            final_str += string[i]
            i += 1
        final_str += string[i]
        i += 1
    elif string[i] == ' ':
        final_str += back_flip(temp)
        final_str += ' '
        temp = ''
        i += 1
    else:
        temp += string[i]
        i += 1

final_str += back_flip(temp)
print(final_str)
