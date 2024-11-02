import sys
input = sys.stdin.readline

x = int(input())
t = 0
d = x
v = 1
while True:
    d -= v
    t += 1
    if d == 0:
        break

    # 속도를 1 더 높여도 괜찮은지
    # 만약 속도를 1 더 높인다면 이후 속도는 계속 줄여야함
    # 남은 거리가 v+1, v, v-1, -2, ..., 2, 1 보다 크거나 같아야 함
    if d >= (v + 1) * (v + 2)  / 2:
        v += 1
    # 속도를 유지하는 경우
    # v, v-1, ..., 2, 1
    elif d >= v * (v + 1) / 2:
        pass

    # 위 둘을 만족하지 않으면 속도는 줄여야
    else:
        v -= 1
print(t)