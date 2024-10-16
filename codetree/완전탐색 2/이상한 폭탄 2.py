import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

r = -1
for i in range(n):
    for j in range(i+1, n):
        # 서로 번호가 같고 거리가 k 내라면 폭발
        if arr[i] == arr[j] and abs(i-j) <= k:
            r = max(r, arr[i])

print(r)