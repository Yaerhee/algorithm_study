# 배열에 10,000개의 정수 삽입
import time
from random import randint

array = []
for _ in range(10000):
    array.append(randint(1, 100)) # 1 ~ 100 사이의 무작위 숫자(정수)

# 선택 정렬 프로그램의 성능 측정
start_time = time.time() # 측정 시작

# 선택 정렬 프로그램 소스 코드
for i in range(len(array)):
    min_index = i # 제일 작은 원소의 idx
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i] # 두 수를 바꿈

end_time = time.time() # 측정 종료
print(f'선택 정렬 성능 측정: {end_time - start_time}')

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()
print(f'기본 정렬 라이브러리 성능 측정: {end_time - start_time}')