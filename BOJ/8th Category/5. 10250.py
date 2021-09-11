import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    num = 1

    for j in range(N // H):
        if N - H > 0:
            num += 1
            N = N - H
    if num < 10:
        print(f'{N}0{num}')
    else:
        print(f'{N}{num}')