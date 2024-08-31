import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
total = sum(arr)

min_sum = sys.maxsize
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            s = arr[i]+arr[j]+arr[k]
            min_sum = min(min_sum, abs(s - (total-s)))

print(min_sum)