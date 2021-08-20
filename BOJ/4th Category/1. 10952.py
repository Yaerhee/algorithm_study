import sys

while True: # 멈춤 조건이 없는 한 무한 루프
    A, B = map(int, sys.stdin.readline().split())
    # while문 밖에 있을 경우 결과값이 무한 출력 ^^

    if A == 0 and B == 0: break # break 선에서 while문 처리 가능
    print(A + B)