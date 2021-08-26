import sys

A, B = list(map(str, sys.stdin.readline().split()))
rA = A[::-1] # (...) 문자열을 뒤집어 출력하는 방법이 이렇게 간단하다니
rB = B[::-1]
print(rA if rA > rB else rB) # 조건문은 어려워

