T = int(input())

for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    max_price = arr[-1] # 가장 마지막 원소로 최댓값 초기화
    benefit = 0
    # 뒤에서부터 순회
    for i in range(n-2, -1, -1):
        if arr[i] < max_price:
            benefit += (max_price - arr[i])
        else:
            max_price = arr[i]

    print("#"+str(t+1), benefit)