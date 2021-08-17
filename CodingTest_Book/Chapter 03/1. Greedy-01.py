# 화폐의 종류가 K개라고 할 때의 시간 복잡도는 O(K)
import sys

n = int(sys.stdin.readline())
count = 0

# 큰 화폐의 개수부터 처리하고 줄여나감
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 남은 돈에서 화폐단위를 나눈 몫 (//로 정수만 남김 -> 동전 개수)
    n %= coin # n은 아직 처리되지 않았으니, 나뉜 화폐단위로 먼저 처리한 후 나머지를 남김
    # ex. 1260원이라 가정했을 때, 첫 coin 단위인 500원으로 나눌 경우 260원이 남음 -> 이게 100원에 있어서의 n이 됨

print(count)