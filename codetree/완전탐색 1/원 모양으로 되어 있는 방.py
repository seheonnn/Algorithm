import sys
input = sys.stdin.readline

n = int(input().strip())
room = []
for _ in range(n):
    room.append(int(input().strip()))

min_sum = sys.maxsize
for i in range(n):
    s = 0
    for j in range(n):
        idx = (i+j) % n
        s += room[idx] * j # 시계 반대방향으로만 움직임
    min_sum = min(min_sum, s)
print(min_sum)
