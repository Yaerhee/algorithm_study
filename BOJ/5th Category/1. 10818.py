import sys

N = int(sys.stdin.readline()) # 정수의 개수
Array = list(map(int, sys.stdin.readline().split()[:N])) # [:N] 으로 N개 까지만 split 하도록 설정

Array.sort()
print(min(Array), max(Array)) # Array의 최소값, 최대값 출력