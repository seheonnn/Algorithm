def solution(scores):
    wanS1, wanS2 = scores[0][0], scores[0][1]
    scores.sort(key=lambda x: (-x[0], x[1]))

    maxPeer = 0
    rank = 1
    for tmp in scores:  # 근무태도 내림차순, 동료평가 오름차순
        if tmp[1] < maxPeer:  # 이미 근무태도는 앞 사람보다 작기 때문에 동료평가만 검사
            if tmp[0] == wanS1 and tmp[1] == wanS2:  # 두 점수 모두 작은 경우가 완호라면 -1 반환
                return -1
            continue  # 나머지 애들은 순위 계산 제외

        if tmp[0] + tmp[1] > wanS1 + wanS2:
            rank += 1
        maxPeer = max(maxPeer, tmp[1])

    return rank