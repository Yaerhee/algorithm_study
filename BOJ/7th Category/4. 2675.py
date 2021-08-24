import sys

T = int(sys.stdin.readline())

for i in range(T):
    inputs = list(map(str, sys.stdin.readline().split()))

    N = int(inputs[0])
    S = inputs[1]

    array = []

    for i in range(len(S)):
        array.append(S[i]*N)

    P = "".join(array) # Array를 구분하는 지점을 없애고 string으로 내용을 합침
    print(P)