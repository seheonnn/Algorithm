import heapq

def solution(jobs):
    time = 0
    total = 0
    idx = 0
    n = len(jobs)

    jobs.sort()
    pq = []
    while idx < n or pq:
        while idx < n and jobs[idx][0] <= time: # 현재 대기큐
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if pq:
            taskTime, start = heapq.heappop(pq)
            time += taskTime
            total += (time - start)
        else:
            time = jobs[idx][0]

    return total // n