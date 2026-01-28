import sys

word_stack = []
cnt = 0
text = sys.stdin.readline().rstrip()

for c in text:
    word_stack.append(c)

while word_stack:
    c = word_stack.pop()

    if c == "=":
        prev = word_stack.pop()
        if prev in ["c", "s"]:
            cnt += 1
            continue
        if prev == "z":
            if word_stack:
                pprev = word_stack.pop()
                if pprev == "d":
                    cnt += 1
            
                else:
                    cnt += 1
                    word_stack.append(pprev)
            else:
                cnt += 1

    elif c == "-":
        prev = word_stack.pop()
        if prev in ["c", "d"]:
            cnt += 1
            continue

    elif c == "j":
        if word_stack:
            prev = word_stack.pop()
            if prev in ["l", "n"]:
                cnt += 1
                continue

            else:
                cnt += 1
                word_stack.append(prev)
                continue
        else:
            cnt += 1
            continue

    else:
        cnt += 1

print(cnt)