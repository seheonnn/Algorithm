from collections import deque

def solution(menu, order, k):
    answer = 0
    queue = deque()
    prev_end = 0
    for i, drink in enumerate(order):
        arrive = i * k
        while queue and queue[0] <= arrive:
            queue.popleft()

        start = max(arrive, prev_end)
        end = start + menu[drink]
        prev_end = end
        queue.append(end)
        answer = max(answer, len(queue))

    return answer