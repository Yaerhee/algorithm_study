import sys

Array = []

for i in range(10):
    Array.append(int(sys.stdin.readline())%42)

print(len(set(Array)))