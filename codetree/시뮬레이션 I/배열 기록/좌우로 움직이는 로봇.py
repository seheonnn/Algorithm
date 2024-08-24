import sys
input = sys.stdin.readline

OFFSET = 500000
n, m = map(int, input().split())
pos_a, pos_b = [0] * (2*OFFSET + 1), [0] * (2*OFFSET + 1)

time_a = 1
for _ in range(n):
    w, di = input().split()
    w = int(w)
    for _ in range(w):
        pos_a[time_a] = pos_a[time_a-1] + (1 if di == "R" else -1)
        time_a += 1

time_b = 1
for _ in range(m):
    w, di = input().split()
    w = int(w)
    for _ in range(w):
        pos_b[time_b] = pos_b[time_b-1] + (1 if di == "R" else -1)
        time_b += 1

# 움직임을 종료한 이후에는 같은 위치에 있어야 함
# 이동이 끝났을 때 길이가 다를 수 있으므로 맞추는 작업
if time_a < time_b:
	for i in range(time_a, time_b):
		pos_a[i] = pos_a[i - 1]
elif time_a > time_b:
	for i in range(time_b, time_a):
		pos_b[i] = pos_b[i - 1]

r = 0
for i in range(1, max(time_a, time_b)):
    if pos_a[i-1] != pos_b[i-1] and pos_a[i] == pos_b[i]:
        r += 1
print(r)