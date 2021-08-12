
H, M = map(int, input().split())
if not (0 <= H <= 23) or not (0 <= M <= 60):
    print("잘못된 입력입니다.")

HM = H * 60 + M - 45

H2 = HM // 60
if H2 == -1:
    H2 = 23

M2 = HM % 60

print(H2, M2)

# 매우 이상적이고 짧고 굵고 예쁜 답(특: 내 머리에선 안나옴)
# M -= 45
#
# if M < 0:
#     H -= 1
#
# print(H%24, M%60)