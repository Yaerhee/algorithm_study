import sys

C = int(sys.stdin.readline())

for _ in range(C):
    data = list(map(int, sys.stdin.readline().split()))

    N = data[0]
    scores = []

    for i in range(N):
        scores.insert(i, data[i+1])

    avr = sum(scores) / len(scores)

    count = 0
    for i in range(N):
        if scores[i] > avr:
            count += 1

    percent = (count / N) * 100

    print(f'{percent:.3f}%') # round( ,3) 으로는 정수로 떨어지는 숫자의 소숫점을 표시할 수 없음에 유의