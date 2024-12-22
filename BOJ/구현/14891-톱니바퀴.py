import sys
from collections import deque

input= sys.stdin.readline

gear = []
for _ in range(4):
    gear.append(deque(list(input().strip())))

k = int(input())

def left(num, direction):
    if num < 0:
        return
    if gear[num][2] != gear[num + 1][6]: # 현재 톱니 바퀴의 2 번째 톱니는 다음 톱니 바퀴의 6 번째 톱니와 맞닿아 있음
        left(num - 1, -direction) # 맞닿은 부분이므로 반대 방향으로 회전
        gear[num].rotate(direction)


def right(num, direction):
    if num > 3:
        return
    if gear[num][6] != gear[num - 1][2]:
        right(num + 1, -direction)
        gear[num].rotate(direction)

for _ in range(k):
    num, d = map(int, input().split())
    num -= 1
    left(num - 1, -d)  # 맞닿은 톱니바퀴는 현재 톱니바퀴와 반대 방향으로 회전함
    right(num + 1, -d)
    gear[num].rotate(d)

r = 0
if gear[0][0] == '1': # 1번 톱니바퀴의 12시 방향이 S극(1)이면 1점
    r += 1
if gear[1][0] == '1':
    r += 2
if gear[2][0] == '1':
    r += 4
if gear[3][0] == '1':
    r += 8

print(r)
