import sys

depth = int(sys.stdin.readline())
for case in range(1, depth+1):
    a, b = map(int, sys.stdin.readline().split())
    # print("Case #", case, ":", a + b) # 음.. 이게 왜 틀렸지?
    # 우선 f-string을 활용하여 {} 내부 변수/ 변수 연산값 출력
    # 띄어쓰기가 섞여있어서 f-string 제출을 강제하려고 오답 처리 한듯!
    print(f'Case #{case}: {a + b}')