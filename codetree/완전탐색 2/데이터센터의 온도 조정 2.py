import sys
input = sys.stdin.readline

n, c, g, h = map(int, input().split())

def get_work(tmp, ta, tb):
    if tmp < ta :
        return c
    elif ta <= tmp <= tb:
        return g
    else:
        return h

arr = []
for _ in range(n):
    ta, tb = map(int, input().split())
    arr.append((ta, tb))

r = -sys.maxsize
for i in range(1001):
    s = 0
    for ta, tb in arr:
        s += get_work(i, ta, tb)
    r = max(r, s)
print(r)
