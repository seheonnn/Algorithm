import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

start = max(arr)
end = sum(arr)
answer = end

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    cur = mid
    for num in arr:
        if cur < num:
            cnt += 1
            cur = mid
        cur -= num
        if cnt > m:
            break
    if cnt <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)