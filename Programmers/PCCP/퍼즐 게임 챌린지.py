def solution(diffs, times, limit):
    answer = float('inf')
    n = len(diffs)
    left, right = 1, max(diffs)

    while left <= right:
        mid = (left + right) // 2

        total = times[0]

        for i in range(1, n):

            if diffs[i] <= mid:
                total += times[i]
            else:
                fails = diffs[i] - mid
                total += fails * (times[i] + times[i - 1]) + times[i]

            if total > limit: break

        if total <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer