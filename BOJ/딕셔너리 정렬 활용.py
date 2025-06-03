def solve(k, expected_table, actual_table):
    actual_score = {num: score for num, score in actual}

    # 우선순위 높은순 정렬
    by_priority = sorted(expected_table, key=lambda x: x[1])[:k]  # k개
    expect_pri_sum1 = sum(x[2] for x in by_priority)
    act_sum1 = sum(actual_score[x[0]] for x in by_priority)
    diff1 = abs(expect_pri_sum1 - act_sum1)

    # 예상점수 내림차순, 같으면 우선순위 기준 오름차순
    by_score = sorted(expected_table, key=lambda x : (-x[2], x[1]))[:k]
    expect_pri_sum2 = sum(x[2] for x in by_score)
    act_sum2 = sum(actual_score[x[0]] for x in by_score)
    diff2 = abs(expect_pri_sum2 - act_sum2)

    return diff1, diff2


expected = [
    (1, 1, 100),
    (2, 3, 30),
    (3, 2, 100),
    (4, 5, 450),
    (5, 4, 2000)
]

actual = [
    (1, 350),
    (2, 30),
    (3, 20),
    (4, 100),
    (5, 1500)
]

# k = 3일 때 우선순위 순으로 계산한 예상점수, 높은 예상점수 순으로 계산한 예상점수, 예상점수가 같으면 우선순위 높은 순
k = 3

print(solve(k, expected, actual))  # ✅ (170, 600)

# d = { 'a': 3, 'b': 1, 'c': 5 }
# sorted(d) # 딕셔너리는 기본적으로 key 기준
# 결과: ['a', 'b', 'c']

# sorted(d.items(), key=lambda x: x[1]) # value기준
# # 결과: [('b', 1), ('a', 3), ('c', 5)]

