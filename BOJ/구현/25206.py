# 구현 - 너의 평점은

import sys

sum = 0
grade = 0 # 학점 * 과목 평점
result = 0
for _ in range(20):
    c, g, s = sys.stdin.readline().split()
    if s == 'P':
        continue

    g = float(g)
    sum += g

    if s == 'A+':
        grade += g * 4.5

    elif s == 'A0':
        grade += g * 4.0

    elif s == 'B+':
        grade += g * 3.5

    elif s == 'B0':
        grade += g * 3.0

    elif s == 'C+':
        grade += g * 2.5

    elif s == 'C0':
        grade += g * 2.0

    elif s == 'D+':
        grade += g * 1.5

    elif s == 'D0':
        grade += g * 1.0

    elif s == 'F':
        grade += g * 0.0

result = grade / sum

print(format(result, ".6f"))