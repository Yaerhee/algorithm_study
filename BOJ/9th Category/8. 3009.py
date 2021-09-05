import sys

x = []
y = []

for i in range(3):
    result_x, result_y = map(int, sys.stdin.readline().split())
    x.append(result_x)
    y.append(result_y)

for i in range(3):
    if x.count(x[i]) == 1:
        result_x = x[i]
    if y.count(y[i]) == 1:
        result_y = y[i]

print(result_x, result_y)
