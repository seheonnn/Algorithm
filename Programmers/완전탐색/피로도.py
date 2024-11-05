import itertools


def solution(k, dungeons):
    answer = -1

    # 모든 순열 생성
    for perm in itertools.permutations(dungeons):
        remain = k  # 현재 남아있는 피로도
        cnt = 0  # 탐험한 던전의 개수

        # 던전 탐험
        for min_stamina, consume_stamina in perm:

            # 남은 피로도가 던전의 최소 필요 피로도보다 더 크면 탐험 가능
            if remain >= min_stamina:
                remain -= consume_stamina
                cnt += 1
            else:
                break  # 던전 탐험 불가능한 경우

        answer = max(answer, cnt)

    return answer