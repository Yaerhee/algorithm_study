import sys

# 특정 좌표 (x, y)에서 직사각형의 가장자리로 빠져나와야 함
# (x, y)를 기준으로 십자 선을 그었을 때, 각기 네 방향의 거리를 가정
# x, y, w-x, h-y가 되는데, 이 네 거리에서 각기 최소값을 구하고
# 가로 최소값, 세로 최소값에서 더 작은 값을 출력하면 해결

x, y, w, h = list(map(int, sys.stdin.readline().split()))
print(min(min(x, w-x), min(y, h-y)))
