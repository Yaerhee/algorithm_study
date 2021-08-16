import sys

starLines = int(sys.stdin.readline())
for stars in range(1, starLines + 1):
    print(stars * '*') 
    # ? 이렇게 쉽게 되다니 ㅋㅋㅋ
    # * 별표 표시하는 만큼 반복문에서 stars 곱해서 출력