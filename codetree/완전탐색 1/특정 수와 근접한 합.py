import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        temp = arr.copy()
        temp[i] = 0
        temp[j] = 0
        min_diff = min(min_diff, abs(s - sum(temp)))
print(min_diff)