def d(n):
    num = int(n)
    for i in list(str(n)): # 숫자를 str list로 분리, 각 자릿수를 더하여 num return
        num += int(i)
    return num


notUniqueArray = set() # 처음부터 중복을 제거할 set 변수 생성

# n을 d(n)의 생성자라고 하는데, 생성자가 없는 숫자를 셀프넘버라고 함

for j in range(1, 10001):
    sengSungJa = d(j)
    if sengSungJa < 10001:
        notUniqueArray.add(sengSungJa) # 생성자가 있는 숫자들을 배열에 추가

for j in range(1, 10001):
    if j not in notUniqueArray:
        print(j) # 생성자가 없는 숫자가 발견되면 바로 출력
