import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()[:N]))
newScores = []

for i in range(N):
    newScores.append(scores[i] / max(scores) * 100)

print(sum(newScores) / len(newScores)) # 않이.. 진짜 average 없어요..?