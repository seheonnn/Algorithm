# import heapq
# import sys

# input = sys.stdin.readline

# n = int(input())
# queue = []

# for i in range(n):
#     age, name = input().split()
#     age = int(age)

#     heapq.heappush(queue, (age, i, name))

# for _ in range(n):
#     age, i, name = heapq.heappop(queue)
#     print(age, name)

import sys

input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    age, name = input().split()
    age = int(age)

    lst.append((age, i, name))

lst = sorted(lst, key=lambda x : (x[0], x[1]))

for tmp in lst:
    print(tmp[0], tmp[2])