# 두 수를 입력받아 각 자릿수 별 곱셈을 출력(0 미반영), 모든 자릿수의 합을 출력

A = int(input())
B = str(input())

first = A * int(B[2])
second = A * int(B[1])
third = A * int(B[0])

print(first, second, third, (first + second * 10 + third * 100), sep='\n')