import heapq

def solution(program):
    answer = [0] * (10 + 1)
    pq = []
    n = len(program)
    idx = 0
    time = 0

    program.sort(key=lambda x: (x[1], x[0]))

    while pq or idx < n:
        while idx < n and program[idx][1] <= time:
            heapq.heappush(pq, (program[idx][0], program[idx][1], program[idx][2]))
            idx += 1

        if pq:
            score, start, tasktime = heapq.heappop(pq)
            wait_time = time - start
            answer[score] += wait_time
            time += tasktime
        else:
            time = program[idx][1]

    answer[0] = time  # 모든 프로그램이 종료되는 시간
    return answer