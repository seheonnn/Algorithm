# 구현 - 통계

import sys
import statistics
from collections import Counter

n = int(sys.stdin.readline())
lst = []

def mean():
    return round(statistics.mean(lst))

def median():
    return statistics.median(lst)

def mode():
    sorted_lst = sorted(lst)
    counter = Counter(sorted_lst)
    mode = counter.most_common()
    if len(mode) == 1:
        return mode[0][0]
    elif mode[0][1] == mode[1][1]:
        return mode[1][0]
    else:
        return mode[0][0]

def ran():
    return max(lst) - min(lst)

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

print(mean())
print(median())
print(mode())
print(ran())


# import sys
#
# n = int(sys.stdin.readline())
# lst = []
#
# def mean():
#     return round(sum(lst) / len(lst))
#
# def median():
#     sorted_lst = sorted(lst)
#     return sorted_lst[len(lst) // 2]
#
# def mode():
#     dic = {}
#     for i in lst:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1
#     mode = max(dic.values())
#     mode_lst = []
#     for i in dic:
#         if mode == dic[i]:
#             mode_lst.append(i)
#     if len(mode_lst) > 1:
#         return sorted(mode_lst)[1]
#     return mode_lst[0]
#
# def ran():
#     return max(lst) - min(lst)
#
# for _ in range(n):
#     lst.append(int(sys.stdin.readline()))
#
# print(mean())
# print(median())
# print(mode())
# print(ran())
