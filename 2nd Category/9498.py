# A = int(input())
# if 90 <= A <= 100: print('A')
# elif 80 <= A <= 89: print('B')
# elif 70 <= A <= 79: print('C')
# elif 60 <= A <= 69: print('D')
# else: print('F')

# 좀더 스마트하게
score = int(input())
if score >= 90: print('A')
elif score >= 80: print('B')
elif score >= 70: print('C')
elif score >= 60: print('D')
else: print('F')