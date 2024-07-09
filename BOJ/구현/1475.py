# 구현 - 방 번호 (딕셔너리)

import sys
import math

n = sys.stdin.readline().strip().replace("6","9")
n = list(map(int, n))

dic = {}

for i in range(10):
    dic[i] = 0
for i in n:
    dic[i] += 1

dic[9] = math.ceil(dic[9] / 2)

result = max(dic.values())

print(result)
