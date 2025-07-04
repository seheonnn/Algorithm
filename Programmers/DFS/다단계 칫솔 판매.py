def dfs(profitMap, parentsMap, seller, profit):
    if seller == '-' or profit < 1: return

    share = profit // 10
    pro = profit - share
    profitMap[seller] += pro
    dfs(profitMap, parentsMap, parentsMap[seller], share)


def solution(enroll, referral, seller, amount):
    answer = []
    n = len(enroll)
    m = len(seller)
    profitMap = {}
    parentsMap = {}

    for i in range(n):
        profitMap.setdefault(enroll[i], 0)
        parentsMap.setdefault(enroll[i], "-")
        parentsMap[enroll[i]] = referral[i]

    for i in range(m):
        dfs(profitMap, parentsMap, seller[i], amount[i] * 100)

    for name in enroll:
        answer.append(profitMap[name])

    return answer