import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

r = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = arr[i]
        x2, y2 = arr[j]
        s = (x1-x2)**2 + (y1-y2)**2
        r = min(r, s)
print(r)