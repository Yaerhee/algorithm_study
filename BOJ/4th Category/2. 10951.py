import sys

# EOF, end of file - 입력이 끝날 때까지 내용을 읽어들이도록 설정
while True: # 멈춤 조건이 없는 한 무한 루프
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except:
        break