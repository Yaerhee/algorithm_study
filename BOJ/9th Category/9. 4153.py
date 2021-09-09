import math
import sys

while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))

    if a == 0 and b == 0 and c == 0:
        break

    # 아 ... 어느 면이 빗변인지 알 수가 없어서 틀렸음 ㅎ_ㅎ
    if a * a + b * b == c * c:
        print('right')
    elif a * a == b * b + c * c:
        print('right')
    elif b * b == a * a + c * c:
        print('right')
    else:
        print('wrong')
