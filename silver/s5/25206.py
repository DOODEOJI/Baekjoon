import sys

lines = []
while True:
    line = sys.stdin.readline().rstrip().split()
    if not line:
        break
    lines.append(line)

grade_dict = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

gsum = 0
ssum = 0
for _, grade, score in lines:
    if score == 'P':
        continue
    gsum += int(grade.strip('.0'))
    ssum += int(grade.strip('.0')) * grade_dict[score]

print('%.6f'%(ssum/gsum))