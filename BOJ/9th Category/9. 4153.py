import math
import sys

while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))

    if a == 0 and b == 0 and c == 0:
        break

    if int(math.sqrt(pow(a, 2) + pow(b, 2))) == c:
         print('right')
    else:
        print('wrong')
