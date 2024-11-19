T = int(input())
for t in range(1, T + 1):
    a, b, c = map(int, input().split())

    cnt = 0
    if b >= c:
        cnt += b - c + 1
        b = c - 1 # b를 c - 1로 조정

    if a >= b:
        cnt += a - b + 1
        a = b - 1 # a를 b - 1로 조정

    if a < 1 or b < 1 or c < 1:
        cnt = -1 # 하나라도 1 미만인 곳이 있으면 조건 만족할 수 없음

    print('#' + str(t), cnt)

# 4
# 3 2 1
# 1 2 3
# 3 5 5
# 5 6 6