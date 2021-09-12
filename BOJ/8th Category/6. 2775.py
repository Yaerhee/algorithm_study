import sys

# 굉장한 1차원적 문제풀이를 했던 내 자신에게 반성... -_-
T = int(sys.stdin.readline())

for case in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    vc = [i for i in range(1, n+1)]
    # 층마다 숫자를 보존한 상태에서 계속 덧셈이 이루어져야 함
    for floor in range(k):  # 매 층을 돌아가면서 호수에 따른 인원을 계산
        # 즉, 아래의 연산이 0 ~ k-1층 번 반복됨에 유의
        for j in range(1, n):
            # 매 floor 마다 이루어지는 연산 한 세트
            # 1을 제외한 두 번째 배열 자리부터, 1 + 첫 번째 자리 연산을 두 번째에 대입
            # 이후 순서는 배열 앞자리 숫자 + 현재 자리 숫자를 연산하는 것으로 연속
            vc[j] += vc[j-1]

    print(vc[-1])
