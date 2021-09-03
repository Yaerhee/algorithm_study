import sys

N = int(sys.stdin.readline())

# N-1 (우선 숫자 1 어치는 빼야 하니까)
# (N-1) % 6 = 5 네? 올! (위에서 1을 빼줬으니 나머지가 6밖에 안남음)
# math.ceil(N / 6)... ㅋㅋㅋ 좋아 신박했어

# N = 58이 있다고 치면... 58 - (1 + 6*1 + 6*2 + 6*3 ...)
# N이 0 이하일 경우 길찾기 성공!

count = 0
while N > 0:
    if count == 0:
        N = N - 1
        count += 1
    N = N - 6 * count
    count += 1

print(count)
