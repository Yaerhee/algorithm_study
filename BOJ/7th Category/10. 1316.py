import sys

N = int(sys.stdin.readline())
words = []
count = 0

for i in range(N):
    words.insert(i, sys.stdin.readline().rstrip())

    print(len(words))
    for j in range(len(words)-1): # range가 증가하고 있을 때 j+1이 범위 초과되지 않도록 -1 처리
        if words[j] != words[j+1]: # 이전 단어와 다음 단어가 일치하지 않을 경우
            pass # 문제 없으므로 통과시킴
        elif words[j] in words[j+1:]: # j을 기준으로 j+1 ~ 끝까지 범위를 살핌
            break # 이전 단어가 나옴 = 중복이니 컷
        else: # 아닐 경우 그룹 단어로 count
            count += 1

print(count)
