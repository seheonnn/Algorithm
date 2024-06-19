# 그리디 - 큰 수의 법칙

# 시도
def sol():
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.sort()
    first = lst[n-1]
    second = lst[n-2]

    result = 0
    while(m > 0):
        result += first * k
        m -= k
        result += second
        m -= 1

    print(result)

# 정답
def ans():
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.sort()
    first = lst[n-1]
    second = lst[n-2]

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result = 0
    result += (count) * first
    result += (m - count) * second

    print(result)
