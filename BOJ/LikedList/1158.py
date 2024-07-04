# Linked List - 요세푸스 문제

from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

queue = deque(range(1, n+1))
k -= 1
result = []
print("<",end="")
for i in range(n):
    queue.rotate(-k)
    if i == n-1:
        print(queue.popleft(), end="")
    else:
        print(queue.popleft(), end=", ")
print(">",end="")