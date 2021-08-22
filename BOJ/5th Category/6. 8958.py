import sys

depth = int(sys.stdin.readline())

for i in range(depth):
    count = 0
    scores = 0
    quiz = list(sys.stdin.readline().rstrip()) # '\n' 제거

    for j in quiz:
        if j == 'O':
            count += 1
            scores += count
        else:
            count = 0

    print(scores)
