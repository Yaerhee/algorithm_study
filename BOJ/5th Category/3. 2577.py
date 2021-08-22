import sys

# enter 단위로 split 하는 방식을 찾아봤지만 그냥 각기 입력받는 것으로 -_-
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = str(A * B * C)

for i in range(10):
    print(result.count(str(i)))