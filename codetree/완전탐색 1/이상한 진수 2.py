import sys

input = sys.stdin.readline

n = input().strip()
m = 0

for i in range(len(n)):
    arr = list(map(int, n))
    # if arr[i] == 1:
    #     arr[i] = 0
    # else:
    #     arr[i] = 1

    arr[i] = 1 - arr[i]

    num = 0
    for i in range(len(arr)):
        num = num * 2 + arr[i]
    if num > m:
        m = num

print(m)