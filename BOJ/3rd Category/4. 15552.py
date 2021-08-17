import sys

depth = int(sys.stdin.readline())
# int(input())
# int(input().split())
# 두 입력 방식을 sys.stdin.readline으로 다르게 입력(빠른 입출력)

for array in range(depth):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)