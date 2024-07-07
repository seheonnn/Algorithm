# 구현 - 프린터 큐

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(enumerate(map(int, sys.stdin.readline().split())))
    order = 1

    while queue:
        x, y = queue.popleft()

        if any(y < q[1] for q in queue): # any() : 하나라도 참이 있으면 True를 반환, 아닌 경우 False 반환
            queue.append((x, y))
        else:
            if x == m:
                print(order)
                break
            order += 1
