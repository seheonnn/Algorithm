# 그리디 - 숫자 카드 게임 (min() 아용)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

def sol():
    n, m = map(int, input().split())
    result = 0
    for _ in range(n):
        lst = list(map(int, input().split()))
        result = max(result, min(lst))

    print(result)

def ans():
    n, m = map(int, input().split())
    result = 0
    for i in range(n):
        data = list(map(int, input().split()))
        min_value = min(data)
        result = max(result, min_value)
    print(result)

sol()
