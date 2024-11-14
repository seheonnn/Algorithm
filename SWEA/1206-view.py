T = 10
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    r = 0

    for i in range(2, n-2):
        max_high = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2]) # 본인 제외 주변 건물들 중 최대 층 구함
        if arr[i] > max_high:
            r += arr[i] - max_high

    print("#" + str(t), r)