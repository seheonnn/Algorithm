# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = list(map(int, input().split()))

# result = -sys.maxsize
# for i in range(n):
#     for j in range(n):
#         if abs(i-j) > 1:
#             result = max(result, lst[i] + lst[j])
# print(result)

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

result = -sys.maxsize
for i in range(n):
    for j in range(i+2, n):
        if result < lst[i] + lst[j]:
            result = lst[i] + lst[j]
print(result)