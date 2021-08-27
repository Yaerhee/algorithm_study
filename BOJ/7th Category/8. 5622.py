import sys

chars = sys.stdin.readline().upper()
dials = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for dial in dials: # dials에 있는 알파벳들을 한 칸씩 불러온 후
    for i in dial: # 각 dial에 있는 문자들을 순회 시키고
        for j in chars: # chars를 처음부터 돌리면서
            if i == j: # i랑 j가 같을 경우(입력한 문자에 맞는 다이얼을 만날 경우)
                time += dials.index(dial) # 다이얼을 돌리는 시간을 계산


# 이전 풀이... 노력은 가상했으나 find를 할 필요가 없었음 ㅎ_ㅎ 아쉽
# for i in dials:
#     for j in str(dials[i]):
#         if chars.find(dials[i][j]) != -1:
#             time += dials[i].index()

print(time)


