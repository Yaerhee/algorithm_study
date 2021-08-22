import sys

N = int(sys.stdin.readline()) # 26
NN = N # 처음 입력된 N 값을 건드리지 않고 수정할 수 있는 숫자가 필요함
count = 0 # 횟수를 더하여 출력하기 위한 변수

while True:
    SUM = NN // 10 + NN % 10  # 각 자릿수를 더한 값 (중간처리)
    # print(SUM, "SUM") # 8, 14, 12, 6
    NNN = (NN % 10) * 10 + SUM % 10
    # SUM 이 10이 넘을 경우 한자릿수로 변환 / 10 미만일 경우 그대로 활용
    # 위에서 NN % 10이 원래의 한자릿수였음 -> 십의자리로 올림

    # print(NNN, "NNN") # 68, 84, 42, 26 [새로운 수]
    count += 1

    if NNN == N: # [새로운 수]가 원본으로 입력된 숫자와 같을 경우
        break

    NN = NNN # 여기서 원본과 같은 숫자였던 NN을 NNN[새로운 수]으로 주입해 줌

print(count)
