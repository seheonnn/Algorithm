# 그리디 - 동전
n = 1260
count = 0

# 큰 단위의 화폐부터
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

# 시간 복잡도 : O(K) / K : 화폐의 종류