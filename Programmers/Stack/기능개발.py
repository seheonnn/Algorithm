from collections import deque


def solution(progresses, speeds):
    answer = []
    queue = deque()  # 작업 완료 일수

    for p, s in zip(progresses, speeds):
        queue.append((100 - p + s - 1) // s)  # 올림

    cur = queue.popleft()
    cnt = 1

    while queue:
        day = queue.popleft()
        if day <= cur:
            cnt += 1
        else:
            answer.append(cnt)
            cur = day
            cnt = 1

    answer.append(cnt)  # 마지막 추가

    return answer