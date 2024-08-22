import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

cnt, m = 1, 1

for i in range(n):
    if i == 0 or a[i] != a[i-1]: # 조건식 순서 주의!
        cnt = 1
    elif a[i] == a[i-1]:
        cnt += 1
    m = max(m, cnt)

print(m)
