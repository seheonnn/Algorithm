import heapq

def solution(n, k, enemy):
    pq = []

    # 무적권이 더 많은 경우
    if k >= len(enemy):
        return len(enemy)

    for i in range(len(enemy)):
        heapq.heappush(pq, enemy[i])

        if len(pq) > k:
            n -= heapq.heappop(pq)

        if n < 0:
            return i

    return len(enemy)