# 세 정수를 입력받아 각 공식에 따른 나머지값 출력(+줄바꿈)

import time
start_time = time.time() # 측정 시작

N = int(input())

for lines in reversed(range(1, N+1)): # 1에서 N까지의 배열을 뒤집음
    print(lines)

end_time = time.time() # 측정 종료
print(f'time: {end_time - start_time}')