# 그리디 - 숫자 카드 게임 (중첩 반복문 아용)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

def sol():

    n, m = map(int, input().split())
    result = 0
    for i in range(n):
        min_val = 10001
        data = list(map(int, input().split()))
        for j in range(m):
            if (min_val > data[j]):
                min_val = data[j]
        if (result < min_val):
            result = min_val
    print(result)


def ans():

    n, m = map(int, input().split())
    result = 0
    for i in range(n):
        data = list(map(int, input().split()))
        min_value = 10001
        for a in data:
            min_value = min(min_value, a)
        result = max(result, min_value)
    print(result)

ans()
