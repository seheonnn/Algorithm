import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

min_sum = sys.maxsize
for i in range(n):
    s = 0
    for j in range(n):
        s += lst[j] * abs(i-j)
    if min_sum > s:
        min_sum = s
print(min_sum)