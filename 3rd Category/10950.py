# int를 입력할 횟수를 먼저 정한 후
depth = int(input())
# 반복문에 정해진 횟수만큼 a, b를 입력
for array in range(depth):
    a, b = map(int, input().split())
    print(a + b) # 입력받는 두 수에 대한 연산 결과 출력