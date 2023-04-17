# 시간 초과 len, sum 등 함수 반복 사용하지 않기
import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []
for _ in range (n) :
    li.append(int(sys.stdin.readline()))

li.sort()
# 평균
mean = round(sum(li) / n)
# 중앙값
median = li[n // 2]
# 최빈값
mode = Counter(li).most_common() # 빈도수 많은 것 2개 출력 (빈도수 순서)
mode_value = 0

if len(mode) == 1:
    mode_value = mode[0][0]
elif mode[0][1] == mode[1][1]:
    mode_value = mode[1][0]
else:
    mode_value = mode[0][0]
# 범위
range_N = li[-1] - li[0]
print(mean)
print(median)
print(mode_value)
print(range_N)