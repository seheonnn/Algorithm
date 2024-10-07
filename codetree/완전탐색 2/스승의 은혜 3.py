import sys

input = sys.stdin.readline

n, b = map(int, input().split())
arr = []
for i in range(n):
    p, s = map(int, input().split())
    arr.append((p, s))

r = 0
for i in range(n):
    total_costs = []
    for j in range(n):
        if i == j:
            total_costs.append(arr[j][0] // 2 + arr[j][1])
        else:
            total_costs.append(arr[j][0] + arr[j][1])

    total_costs.sort()  # 합친 비용을 기준으로 정렬
    s = 0
    cnt = 0
    for cost in total_costs:
        if s + cost > b:
            break
        s += cost
        cnt += 1

    r = max(r, cnt)

print(r)
