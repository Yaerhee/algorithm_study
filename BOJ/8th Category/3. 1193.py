import sys

X = int(sys.stdin.readline())

num = 0
count = 0

while X - count > 0:        # count가 X와 같거나 클 때까지
    num += 1            # 1, 2, 3, 4, ...
    count += num        # 1, 3, 6, 10, ... (중첩하여 더함)

count -= num            # 반복문이 끝나고 난 뒤 num을 빼 줌 ex. 10 - 4 = 6

if num % 2 == 0:        # num이 짝수일 때
    # 분자가 늘어나고, 분모가 줄음
    print(f'{X - count}/{1 + (num - (X - count))}')
else:
    # 분모가 늘어나고, 분자가 줄음
    print(f'{num - (X - count) + 1}/{X - count}')
