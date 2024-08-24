import sys
input = sys.stdin.readline

n, m = map(int, input().split())
OFFSET = 1000000 # 크기 주의!
pos_a, pos_b = [0] * (OFFSET + 1), [0] * (OFFSET + 1)

# 시간별 A의 위치 기록
time_a = 1
for _ in range(n):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a-1] + (1 if d == "R" else -1)
        time_a += 1

# 시간별 B의 위치 기록
time_b = 1
for _ in range(m):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b-1] + (1 if d == "R" else -1)
        time_b += 1

r = -1
for i in range(1, max(time_a, time_b)): # 1초부터 시작
    if pos_a[i] == pos_b[i]:
        r = i
        break
print(r)
