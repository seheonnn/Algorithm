answer = float('inf')


def backtracking(picks, minerals, dic, arr, tired, idx):
    global answer

    if tired >= answer: return  # 현재 피로도가 이미 answer보다 크면 스킵

    if idx >= len(minerals) or sum(picks) == 0:
        answer = min(answer, tired)
        return

    for i in range(3):
        if picks[i] > 0:

            cur = 0
            end = min(idx + 5, len(minerals))  # 곡괭이 하나 선택하면 5개 연속으로 써야
            for j in range(idx, end):
                cur += arr[i][dic[minerals[j]]]

            picks[i] -= 1
            backtracking(picks, minerals, dic, arr, tired + cur, end)
            picks[i] += 1


def solution(picks, minerals):
    global answer
    dic = {"diamond": 0, "iron": 1, "stone": 2}
    arr = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    backtracking(picks, minerals, dic, arr, 0, 0)
    return answer