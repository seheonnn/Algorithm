def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for idx, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            prev = stack.pop()
            answer[prev] = idx - prev

        stack.append(idx)

    while stack:
        idx = stack.pop()
        answer[idx] = n - idx - 1

    return answer