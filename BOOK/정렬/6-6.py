# 정렬 - 계수 정렬 O(N + K) N : 데이터의 개수 / K : 데이터 중 최대값의 크기

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt = [0] * (max(array) + 1)

for i in range(len(array)):
    cnt[array[i]] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end=' ')