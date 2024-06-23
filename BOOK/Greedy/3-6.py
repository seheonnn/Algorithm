# 그리디 - 1이 될 때까지

def sol():
    return

def ans():
    n, k = map(int, input().split())
    result = 0

    while True:
        target = (n//k) * k
        result += (n - target)
        n = target
        if n < k:
            break
        result += 1
        n //= k

    result += (n - 1)
    print(result)

ans()
