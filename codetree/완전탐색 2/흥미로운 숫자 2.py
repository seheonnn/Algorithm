import sys

input = sys.stdin.readline

x, y = map(int, input().split())
r = 0

for i in range(x, y + 1):

    num = i
    arr = [0] * 10  # 0~9 숫자 개수 저장 배열
    le = 0  # 수 길이

    while num > 0:
        arr[num % 10] += 1
        num //= 10
        le += 1

    is_inter = False  # 흥미로운 숫자인지
    for i in arr:
        if i == le - 1:
            is_inter = True

    if is_inter:
        r += 1

print(r)