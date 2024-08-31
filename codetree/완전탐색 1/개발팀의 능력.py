import sys

input = sys.stdin.readline

n = 5
arr = list(map(int, input().split()))
min_diff = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):

        for k in range(n):
            for l in range(k + 1, n):

                if i == k or i == l or j == k or j == l:
                    continue

                sum1 = arr[i] + arr[j]
                sum2 = arr[k] + arr[l]
                sum3 = sum(arr) - sum1 - sum2

                if sum1 != sum2 and sum2 != sum3 and sum1 != sum3:
                    r = abs(sum1 - sum2)
                    r = max(r, abs(sum2 - sum3))
                    r = max(r, abs(sum3 - sum1))
                    min_diff = min(min_diff, r)

if min_diff == sys.maxsize:
    print(-1)
else:
    print(min_diff)