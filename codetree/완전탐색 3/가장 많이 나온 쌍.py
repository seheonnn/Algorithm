import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(m):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = 0
# 두 수를 선택하여
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cnt = 0
        for a, b in arr:
            if (i, j) in [(a,b), (b,a)]: # 구간 확인
                cnt+=1
        ans = max(ans, cnt)
print(ans)