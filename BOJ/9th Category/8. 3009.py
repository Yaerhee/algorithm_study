import sys

x = []
y = []

for i in range(3):
    result_x, result_y = map(int, sys.stdin.readline().split())
    x.append(result_x)
    y.append(result_y)

for j in range(3):
    if x.count(x[i]) == 1:
        result_x = x[j]
    if y.count(y[i]) == 1:
        result_y = y[j]

print(result_x, result_y)