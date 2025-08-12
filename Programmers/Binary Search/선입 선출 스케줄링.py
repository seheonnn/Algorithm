def cnt_jobs(time, cores):  # 현재 시간에 몇 개의 작업이 처리되었는지
    s = 0
    for core in cores:
        s += ((time // core) + 1)  # 0초 작업 포함
    return s


def solution(n, cores):
    if n <= len(cores):
        return n

    start, end = 0, max(cores) * n
    min_time = end

    while start <= end:
        mid = (start + end) // 2
        total = cnt_jobs(mid, cores)
        if total >= n:
            min_time = mid
            end = mid - 1
        else:
            start = mid + 1

    jobs_done = 0
    for core in cores:
        jobs_done += (((min_time - 1) // core) + 1)

    for i, core in enumerate(cores):
        if min_time % core == 0:
            jobs_done += 1
            if jobs_done == n:
                return i + 1

    return jobs_done