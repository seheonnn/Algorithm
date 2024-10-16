import sys

input = sys.stdin.readline
MAX = sys.maxsize

t, a, b = map(int, input().split())
arr = []
for i in range(t):
    c, x = input().split()
    arr.append((c, x))

r = 0
for i in range(a, b + 1):
    distance_s = MAX
    distance_n = MAX

    # 위치와 함께 입력되므로 위치를 반복할 필요 X
    for p, q in arr:
        q = int(q)

        if p == 'S':
            distance_s = min(distance_s, abs(q - i))
        else:  # N인 경우
            distance_n = min(distance_n, abs(q - i))

    if distance_s <= distance_n:
        r += 1
print(r)