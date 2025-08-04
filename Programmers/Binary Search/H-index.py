def solution(citations):
    answer = 0
    start, end = 0, max(citations)
    while start <= end:
        mid = (start + end) // 2

        # 인용 >= 기준
        cnt = sum(1 for num in citations if num >= mid)

        if cnt >= mid:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer