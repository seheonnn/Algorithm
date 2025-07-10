import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

def check(k):
    target = None
    for i in range(0, n, k):
        seg = lst[i :i + k]
        seg_min = min(seg)
        seg_max = max(seg)
        tmp = seg_min + seg_max
        if target is None:
            target = tmp
        elif target != tmp:
            return False
    return True

result = 0
for k in range(1, n):
    if n % k == 0:
        if check(k):
            result = 1
print(result)