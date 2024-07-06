# Linked List - 풍선 터뜨리기

from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split())))
result = []

while queue:
    i, j = queue.popleft()
    result.append(i + 1)

    if j > 0:
        queue.rotate(-(j - 1))
    elif j < 0:
        queue.rotate(-j)

print(" ".join(map(str, result)))
