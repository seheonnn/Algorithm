def solution(data, ext, val_ext, sort_by):
    answer = []

    type_sort = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    data = sorted(data, key=lambda x: x[type_sort[sort_by]])

    for v in data:
        if v[type_sort[ext]] < val_ext:
            answer.append(v)

    return answer