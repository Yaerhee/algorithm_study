import sys

N = int(sys.stdin.readline())
qty = 0

while N >= 0:
    if N % 5 == 0:
        # 5kg 단위로 나누어 떨어지는 경우
        qty += (N // 5)  # 5로 나눈 몫을 수량으로
        break
    else:
        N -= 3
        if N < 0:
            qty = -1
            break
        else:
            qty += 1

print(qty)
