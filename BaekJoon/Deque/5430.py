import sys
from collections import deque
t = int(sys.stdin.readline())
for i in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    # rstrip() 우측 끝 개행문자 제거
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")

    queue = deque(arr)
    # 뒤집는 횟수 세기 -> 홀수일 때만 뒤집음. 매번 뒤집으면 성능 저하.
    rev_cnt = 0

    if n == 0:
        queue = []
    for j in p:
        if j == 'R':
            rev_cnt += 1
        elif j == 'D':
            if len(queue) == 0:
                print("error")
                break
            else:
                if rev_cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if rev_cnt % 2 == 0:
            # "?".join(deque()) 하면 deque 의 요소들 사이사이에 ? 들어감. deque 요소도 string 이어야 함.
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")

