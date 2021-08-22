# import sys
#
#
# def solve(a: list) -> int:
#     ans = 0
#     for i in range(len(a)):
#         ans += int(a[i])
#     return ans
#
#
# print(solve(list(sys.stdin.readline().split())))

def solve(a):
    return sum(a)

# 정수 N개에 대한 condition도 상세히 적혀있지 않고,
# "입력 받아야 하는지"의 여부나, 매 줄마다의 결과가 필요한지 등의 설명이 없음.
# 설명이 간결한 것에 비해 풀이 해야하는 코드에 대한 조건이 매우 애매한 것 같다고 느낌