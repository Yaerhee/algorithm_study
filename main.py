import sys

chars = sys.stdin.readline().upper()
dials = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in dials:
    for j in str(dials[i]):
        if chars.find(dials[i][j]) != -1:
            time += dials[i].index()

print(time)


