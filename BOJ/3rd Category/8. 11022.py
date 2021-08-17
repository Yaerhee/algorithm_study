import sys

depth = int(sys.stdin.readline())
for case in range(1, depth + 1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{case}: {a} + {b} = {a + b}')