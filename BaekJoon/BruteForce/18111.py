# 마인크래프트
# list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
import sys
from collections import Counter

n, m, inven = map(int, sys.stdin.readline().split())
blocks = []
for _ in range(n): blocks += map(int, sys.stdin.readline().split())
height, time = 0, 500*500*2*257

min_h = min(blocks)
max_h = max(blocks)
_sum = sum(blocks)
block = dict(Counter(blocks))

for i in range(min_h, max_h + 1):
    if _sum + inven >= i * n * m: # 가지고 있는 블럭의 수가 i 높이의 평평한 땅의 전체 블럭 개수보다 커야 함.
        cur_time = 0
        for key in block:
            if key > i:
                cur_time += (key - i) * block[key] * 2 # key에서 제거해야 하는 높이 차이 * 해당 높이 차이만큼 제거해야 하는 블럭 수 * 2초
            elif key < i:
                cur_time += (i - key) * block[key]
        if cur_time <= time:
            time = cur_time
            height = i

print(time, height)