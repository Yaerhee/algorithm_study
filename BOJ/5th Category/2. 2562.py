import sys

Array = []

for i in range(9):
    Array.append(int(sys.stdin.readline()))

print(max(Array), Array.index(max(Array)) + 1, sep='\n')
