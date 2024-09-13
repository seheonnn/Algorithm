import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

r = 0
for i in range(n):
    o = False
    for j in range(n):
        if i == j:
            continue

            # 겹치는 경우
            # 1. i일 때 x1이 j일 때 x1보다 큰지만 x2는 작은 경우
            # 2. i일 때 x1이 j일 때 x1보다 작지만 x2는 큰 경우
        if (arr[i][0] <= arr[j][0] and arr[i][1] >= arr[j][1]) or (arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1]):
            o = True
            break
    if o == False:
        r += 1
print(r)