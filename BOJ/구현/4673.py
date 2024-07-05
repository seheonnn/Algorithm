# 구현 - 셀프 넘버

n = 10000

def d(n):
    result = n
    while n > 0:
        result += (n % 10)
        n //= 10
    return result

lst = [0 for _ in range(n+1)]

for i in range(1, n+1):
    num = d(i)
    if num <= n:
        lst[num] = 1

for i in range(1, n+1):
    if lst[i] != 1:
        print(i)

# lst = list(range(1, n+1))
# s = set()
#
# for i in lst:
#     num = d(i)
#     if num <= n:
#         s.add(num)
#
# ans = [x for x in lst if x not in s]
# for i in ans:
#     print(i)
