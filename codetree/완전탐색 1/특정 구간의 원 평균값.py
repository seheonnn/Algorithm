import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        sub = arr[i:j+1] # 원소가 하나인 경우도 포함
        mean = sum(sub) / len(sub)
        if mean in sub:
            cnt += 1
print(cnt)
