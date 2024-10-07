# import sys
# input = sys.stdin.readline

# r = -sys.maxsize
# x, y = map(int, input().split())
# for i in range(x, y+1):
#     m_sum = 0
#     a = i
#     while a > 0:
#         m_sum += a % 10
#         a //= 10
#     r = max(r, m_sum)
# print(r)

import sys
input = sys.stdin.readline

def get_sum(n):
    if n < 10:
        return n
    else:
        return get_sum(n // 10) + (n % 10)

r = -sys.maxsize
x, y = map(int, input().split())

for i in range(x, y+1):
    r = max(r, get_sum(i))
print(r)
