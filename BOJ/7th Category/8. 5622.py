import sys

chars = sys.stdin.readline().upper()
dials = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for dial in dials:
    for i in dial:
        for j in chars:
            if i == j:
                time += dials.index(dial)

print(time)


