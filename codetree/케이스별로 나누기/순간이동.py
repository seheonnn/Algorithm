import sys
input = sys.stdin.readline

A, B, x, y = map(int, input().split())

min_d = sys.maxsize
# 아래 세 경우 중 가장 이동거리가 짧은 경우를 구하면 됨
# A -> B
min_d = min(min_d, abs(B - A))

# A -> x 순간이동 y -> B
min_d = min(min_d, abs(x - A) + abs(B - y))

# A -> y 순간이동 x -> B
min_d = min(min_d, abs(y - A) + abs(B - x))

print(min_d)