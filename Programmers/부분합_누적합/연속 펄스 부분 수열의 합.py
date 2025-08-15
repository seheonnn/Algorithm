def solution(sequence):
    n = len(sequence)

    pulse1 = [-sequence[i] if i % 2 == 0 else sequence[i] for i in range(n)]
    pulse2 = [sequence[i] if i % 2 == 0 else -sequence[i] for i in range(n)]

    max_sum1 = cur_sum1 = pulse1[0]
    max_sum2 = cur_sum2 = pulse2[0]

    for i in range(1, n):
        cur_sum1 = max(pulse1[i], cur_sum1 + pulse1[i])  # 새로 시작 vs 더하기
        max_sum1 = max(max_sum1, cur_sum1)

        cur_sum2 = max(pulse2[i], cur_sum2 + pulse2[i])
        max_sum2 = max(max_sum2, cur_sum2)

    return max(max_sum1, max_sum2)