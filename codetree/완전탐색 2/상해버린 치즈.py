import sys

input = sys.stdin.readline

n, m, d, s = map(int, input().split())

# 치즈를 먹은 기록
d_lst = [list(map(int, input().split())) for _ in range(d)]
# 아픈 기록
s_lst = [list(map(int, input().split())) for _ in range(s)]

# 약이 최대 몇 개 필요한지 = 아플 수 있는 최대 사람의 수
r = 0

# i 번째 치즈가 상한 경우
for i in range(1, m + 1):
    # time ->  인덱스 : 사람, 값 : 치즈를 먹은 시간
    time = [0] * (n + 1)
    for p, m, t in d_lst:
        # i 번째 치즈인 경우에만
        if m != i:
            continue

        # p 사람이 i 번째 치즈를 처음 먹었거나
        if time[p] == 0:
            time[p] = t
        # 기록된 시간보다 더 빨리 먹었다면, p가 먹은 시간 갱신
        elif time[p] > t:
            time[p] = t

    # i 번째 치즈가 상했다고 가정
    possible = True

    for p, t in s_lst:
        # p 가 치즈를 먹지 않았거나 치즈를 먹은 시간(time[p])보다 더 빨리 아프다면 모순임
        if time[p] == 0 or time[p] >= t:
            possible = False
            break

    # i 번째 치즈가 상한 것이 맞다면
    pill = 0
    if possible:
        for j in range(1, n + 1):
            # 상한 치즈를 먹은 사람의 수만큼 약이 필요함
            if time[j] != 0:
                pill += 1

    r = max(r, pill)

print(r)
