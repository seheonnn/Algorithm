T = int(input())
for _ in range(T):
    N, P = map(int, input().split())

    floor = 0
    for i in range(1, N + 1):
        floor += i
        if floor == P:
            floor -= 1  # 가능한 높은 층수를 구해야 하므로 더했을 때 폭탄층이라면 1 뺌
    print(floor)