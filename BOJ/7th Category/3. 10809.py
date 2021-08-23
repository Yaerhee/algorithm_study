import sys

# alphabets = []
# ASCII = 97
# while ASCII < 123: # z 이후는 커엇!
#     alphabets.append(chr(ASCII))
#     ASCII += 1

S = sys.stdin.readline()
alphabets = list(range(97, 123))

# result = []

for i in alphabets:
    # result.append(S.find(chr(alphabets[i]))) # S를 두고 알파벳 다 돌려서 찾아보기
    print(S.find(chr(i)), end=' ')


# print(str(result)[1:-1]) # result를 문자열로 변환한 후, 양쪽의 괄호를 지움!
