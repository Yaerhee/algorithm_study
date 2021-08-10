# A, B = map(int, input().split())
# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# else:
#     print('==')
#
# 삼항 연산자?
# 조건식 1이 참일때 값 & [if 조건식 1] & 조건식 2가 참일때 값 & [if 조건식 2] & 모두 거짓일 때 값
A, B = map(int, input().split())
print('>') if A > B else print('<') if A < B else print('==')