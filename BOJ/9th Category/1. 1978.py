import sys

N = int(sys.stdin.readline())
Array = map(int, sys.stdin.readline().rstrip().split())

sosu = 0

for i in Array:
    dividable = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                dividable += 1
        if dividable == 0:
            sosu += 1

print(sosu)