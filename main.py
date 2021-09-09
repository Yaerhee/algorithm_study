import math
import sys

while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))

    if a == 0 and b == 0 and c == 0:
        break

    if a * a + b * b == c * c:
        print('right')
    elif a * a == b * b + c * c:
        print('right')
    elif b * b == a * a + c * c:
        print('right')
    else:
        print('wrong')
