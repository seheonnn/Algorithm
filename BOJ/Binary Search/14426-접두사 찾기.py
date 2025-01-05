import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
prefix = []
for _ in range(n):
    arr.append(input().strip())
for _ in range(m):
    prefix.append(input().strip())

arr.sort()

def binary_search(target, start, end):

    if start > end:
        return False
    mid = (start + end) // 2

    # if arr[mid][0: len(target)] == target:
    # ** startswith ** 기억 !!
    if arr[mid].startswith(target):
        return True
    elif arr[mid] < target:
        return binary_search(target, mid+1, end)
    else:
        return binary_search(target, start, mid-1)

cnt = 0
for s in prefix:
    if binary_search(s, 0, len(arr) - 1):
        cnt += 1
print(cnt)
