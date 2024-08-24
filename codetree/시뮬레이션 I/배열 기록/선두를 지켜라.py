import sys
input = sys.stdin.readline

OFFSET = 1000000 # 범위 주의
n, m = map(int, input().split())
pos_a, pos_b = [0] * (OFFSET + 1), [0] * (OFFSET + 1)

dis_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_a[dis_a] = pos_a[dis_a - 1] + v
        dis_a += 1

dis_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_b[dis_b] = pos_b[dis_b - 1] + v
        dis_b += 1

r = 0
for i in range(1, dis_a):
    if pos_a[i-1] >= pos_b[i-1] and pos_a[i] < pos_b[i] :
        r += 1
    elif pos_a[i-1] <= pos_b[i-1] and pos_a[i] > pos_b[i] :
        r += 1

print(r-1)
