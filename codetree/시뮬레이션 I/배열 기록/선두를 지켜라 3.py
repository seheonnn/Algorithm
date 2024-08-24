import sys
input = sys.stdin.readline

OFFSET = 1000000
n, m = map(int, input().split())
pos_a, pos_b = [0] * (OFFSET + 1), [0] * (OFFSET + 1)

time_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a-1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b-1] + v
        time_b += 1

r = 0
for i in range(1, max(time_a, time_b)):
    if pos_a[i-1] > pos_b[i-1] and pos_a[i] < pos_b[i]: # a 혼자 명예 전당 -> b 혼자 명예 전당
        r += 1
    elif pos_a[i-1] < pos_b[i-1] and pos_a[i] > pos_b[i]: # b 혼자 명예 전당 -> a 혼자 명예 전당
        r += 1
    elif pos_a[i-1] != pos_b[i-1] and pos_a[i] == pos_b[i]: # a, b 둘 중 하나가 명예 전당 -> 둘 다 명예 전당
        r += 1
    elif pos_a[i-1] == pos_b[i-1] and pos_a[i] != pos_b[i]: # 둘 다 명예 전당 -> 둘 중 하나 명예 전당
        r += 1
print(r)
