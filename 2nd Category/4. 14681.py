A = int(input())
B = int(input())
# 줄바꿈 구현은 단순 input() / print() 입력으로도 충분하다!
if A >= 0 and B >= 0:
    print(1)
elif A < 0 and B >= 0:
    print(2)
elif A < 0 and B < 0:
    print(3)
else:
    print(4)