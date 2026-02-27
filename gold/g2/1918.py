import sys 

expr = sys.stdin.readline().rstrip()

prior = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2,
    "(" : 3
}

e_stack = []
final = ""
bracket = 0

for e in expr:
    if e in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        final += e

    elif e == ")":
        bracket -= 1
        while e_stack:
            f = e_stack.pop()
            if f == "(":
                break  
            final += f

    elif e == "(":
        bracket += 1
        e_stack.append(e)

    else:
        if e_stack and not bracket:
            while e_stack and prior[e_stack[-1]] >= prior[e]:
                f = e_stack.pop()
                final += f
            e_stack.append(e)

        elif bracket:
            while e_stack and prior[e_stack[-1]] >= prior[e]:
                if e_stack[-1] == "(":
                    break
                f = e_stack.pop()
                final += f
            e_stack.append(e)

        else:
            e_stack.append(e)


while e_stack:
    final += e_stack.pop()

print(final)