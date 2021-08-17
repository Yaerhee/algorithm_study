N = int(input())
# for lines in range(N, 0, -1): # N에서 1까지 "역순"으로 숫자 생성
#     print(lines)

for lines in reversed(range(1, N+1)): # 1에서 N까지의 배열을 뒤집음
    print(lines)