# 구현 - 수열의 정렬

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

b = sorted(a)

for i in a:
    idx = b.index(i)
    b[idx] = n+1 # 중복된 값 처리를 위해 인덱스 찾은 후 배열과 상관없는 값으로 바꿈
    print(idx, end=" ")