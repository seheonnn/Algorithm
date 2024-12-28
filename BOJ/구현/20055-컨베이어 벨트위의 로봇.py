import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
robot = deque(list(map(int, input().split()))) # 내구도
belt = deque([0] * n)
r = 0

while True:
    r += 1

    robot.rotate(1) # rotate(양수) 우측으로 한 칸 돌림
    belt.rotate(1)

    belt[n-1] = 0 # 내리는 위치의 로봇 내림
    for i in range(n - 2, -1, -1): # n-2 시작 이유 : 가장 먼저 올라간 로봇부터 이동이 가능하면 이동해야 함
        if belt[i] and belt[i + 1] == 0 and robot[i + 1] > 0:
            belt[i], belt[i + 1] = 0, 1
            robot[i + 1] -= 1

    belt[n - 1] = 0 # 이동후 내리는 위치(n - 1)에 도달한 로봇은 제거

    if robot[0] > 0: #
        belt[0] = 1 # 올리는 위치(0)에 도달하고 내구성이 1이상이면
        robot[0] -= 1 # 로봇을 올리고 내구도 1 감소

    if robot.count(0) >= k: # 내구도가 0인 칸의 개수가 k개 이상이면 즉시 종료
        break

print(r)
