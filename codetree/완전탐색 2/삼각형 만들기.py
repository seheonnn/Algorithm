import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

r = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            x3, y3 = arr[k]

            # x값이나 y값이 같은 쌍이 있는 경우에만 넓이를 계산해야
            if (x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3):
                s = abs((x1*y2 + x2*y3 + x3*y1)-(x2*y1 + x3*y2 + x1*y3))
                r = max(r, s)
print(r)