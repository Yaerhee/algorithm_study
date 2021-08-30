import sys

N = int(sys.stdin.readline())
count = 0

for i in range(N):
    words = sys.stdin.readline().rstrip()
    for j in range(len(words)):
        if j != len(words)-1:
            if words[j] == words[j+1]: # 이전 단어와 다음 단어가 일치할 경우
                continue # 계속 돌림
            elif words[j] in words[j+1:]: # j을 기준으로 j+1 ~ 끝까지 범위를 살핌
                break # 이전 단어가 나옴 = 중복이니 컷
        else: # 아닐 경우 그룹 단어로 count
            count += 1

print(count)
