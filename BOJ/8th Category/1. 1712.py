import sys

# print(170 * 11 - (1000 + 70 * 11)) # <- 이게 손익분기점
# C * qty - (A+ B * qty))

# print(-1000+(170-70)*11)
# (C-B) * qty - A

A, B, C = list(map(int, sys.stdin.readline().split()))

qty = 0


if qty >= 0:
    try:
        qty = A // (C - B)
        # print(f'{qty} = {A} // ({C} - {B})')
        qty += 1

        if qty < 0:
            qty = -1

    except ZeroDivisionError:
        qty = -1

print(qty)
