import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input().strip()))
ans = 0

for i in range(1, 10001):
    cnt = 0
    for x in arr:
        if i <= x <= i+k: # 구간 [i, i+k] 사이에 있는 값 세기
            cnt+= 1
    ans = max(ans, cnt)
print(ans)