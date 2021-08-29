import sys

word = sys.stdin.readline().rstrip()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 크로아티아 알파벳을 변경해서 입력하는 과정에 집중하는 것이 아니라
# 달랐던 알파벳 묶음을 검색해서 해당 묶음이 한 알파벳일 경우
# 갯수를 바로 측정해주도록 함

for i in croatian:
    word = word.replace(i, '*')

# 변형된(원래 크로아티아어 상의) 알파벳 개수 + 실제 알파벳 개수 count
print(len(word))

