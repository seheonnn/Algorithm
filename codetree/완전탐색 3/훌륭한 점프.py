import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX = 100 # k 최댓값

def is_possible(l):
    idx = 0
    for i in range(1, n):
        if arr[i] <= l:
            if i - idx > k:
                return False
            idx = i
    return True

for i in range(max(arr[0], arr[n-1]), MAX + 1):
    if is_possible(i):
        print(i)
        break