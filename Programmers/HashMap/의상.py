def solution(clothes):
    dic = {}
    for cloth, category in clothes:
        if category not in dic:
            dic[category] = 1
        else:
            dic[category] += 1

    answer = 1
    for key, value in dic.items():
        answer *= (value + 1)

    return answer - 1
