import sys
input = sys.stdin.readline

n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

min_cost = sys.maxsize
# 전체에 대하여 t만큼의 구간씩 모두 h로 만들면서 최소 비용을 구할 수 있음
for i in range(n-t + 1):
    cost = 0
    for j in range(i, i+t):
        cost += abs(arr[j] - h)

    min_cost = min(min_cost, cost)
print(min_cost)