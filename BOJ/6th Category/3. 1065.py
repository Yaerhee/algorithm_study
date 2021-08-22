import sys

def def_hansu(n):
    hansu = 0
    for i in range(1, n + 1): # 1부터 n 숫자의 범위까지 탐색
        N = list(map(int, str(i))) # 각 자릿수 쪼개기
        if i < 100: # 한 자릿수 / 두 자릿수 일 경우
            hansu += 1 # 모두 한수이기 때문에 전부 count
        elif N[0] - N[1] == N[1] - N[2]: # 등차수열의 조건을 만족할 경우 한수로 count
            hansu += 1
    return hansu

n = int(sys.stdin.readline())
print(def_hansu(n))