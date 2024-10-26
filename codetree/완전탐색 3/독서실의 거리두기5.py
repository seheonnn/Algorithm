import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(input().strip())  # str -> list

r = sys.maxsize
ans = 0
for i in range(n):
    if arr[i] == '0':
        arr[i] = '1'

        r = sys.maxsize
        for j in range(n):
            for k in range(j + 1, n):
                if arr[j] == '1' and arr[k] == '1':
                    r = min(r, k - j)

        ans = max(ans, r)
        arr[i] = '0'

print(ans)