# 그리디 - 1이 될 때까지

def sol():
    n, k = map(int, input().split())
    cnt = 0

    while n > 1:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        cnt += 1
    print(cnt)

def ans():
    n, k = map(int, input().split())
    cnt = 0

    while n >= k:
        while n % k != 0:
            n -= 1
            cnt += 1
        n //= k
        cnt += 1

    while n > 1:
        n -= 1
        cnt += 1
    print(cnt)

sol()
