import heapq

def solution(ability, number):
    pq = ability[:]
    heapq.heapify(pq)

    for _ in range(number):
        num1 = heapq.heappop(pq)
        num2 = heapq.heappop(pq)
        heapq.heappush(pq, num1 + num2)
        heapq.heappush(pq, num1 + num2)

    return sum(pq)