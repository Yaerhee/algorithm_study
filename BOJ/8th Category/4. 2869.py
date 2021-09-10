import math
import sys

A, B, V = list(map(int, sys.stdin.readline().split()))

# 단순 반복문이 아니라 "시간 제한"이 있어 한 큐에 푸는 것이 중요한 문제..

# 걸리는 일 수 = 미끄러지고 나서 남은 미터 / 올라간 미터에서 미끄러진 미터

# days = V / (A-B)일 경우 위치에 도달한 후에도 다시 내려가게 될 수 있음
# days = (V-B) / (A-B)로 내려와 있는 상황을 가정하고 시작
# 전부 오르고 나면 미끄러지지 않음 -> B에 대한 계산은 이 때 무효임
days = (V-B)/(A-B)
print(math.ceil(days)) # 소숫점 올림 <-> floor