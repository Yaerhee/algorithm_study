import sys

starLines = int(sys.stdin.readline())

for stars in range(1, starLines + 1):
    print((starLines - stars) * ' ' + stars * '*')
    # 총 범위에서 별표가 제외된 칸은 빈칸으로 채우면 됨