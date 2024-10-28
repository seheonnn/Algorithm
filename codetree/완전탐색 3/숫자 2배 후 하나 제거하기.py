import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_diff = sys.maxsize

for i in range(n):
    arr[i] *= 2  # 현재 수 2배

    for j in range(n):
        remain_arr = []
        for k in range(n):
            if k != j:  # j 는 제외
                remain_arr.append(arr[k])

        sum_diff = 0
        for k in range(n - 2): # 하나를 제외했으므로 전체는 n-1개임
            sum_diff += abs(remain_arr[k + 1] - remain_arr[k])

        min_diff = min(min_diff, sum_diff)

    arr[i] //= 2  # 2배한 수 원상복구

print(min_diff)