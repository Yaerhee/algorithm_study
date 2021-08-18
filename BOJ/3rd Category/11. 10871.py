import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if X > A[i]:  # end=' '로 개행 방지
        print("%d" %A[i], end=" ")

