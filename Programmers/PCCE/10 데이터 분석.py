def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    data.sort(key=lambda x:x[dic[sort_by]])
    for d in data:
        if d[dic[ext]] < val_ext:
            answer.append(d)
    return answer