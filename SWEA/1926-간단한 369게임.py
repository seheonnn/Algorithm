# n = int(input())
# for i in range(1, n+1):
#     lst = list(str(i))
#     if '3' in lst or '6' in lst or '9' in lst:
#         tmp = 0
#         tmp += lst.count('3')
#         tmp += lst.count('6')
#         tmp += lst.count('9')
#         print('-' * tmp, end=" ")
#     else:
#         print(i, end=" ")


# n = int(input())
# for i in range(1, n + 1):
#     cnt = 0
#     for num in str(i):
#         if num in '369':
#             cnt+= 1
#     if cnt > 0:
#         print('-' * cnt, end=" ")
#     else:
#         print(i, end=" ")


n = int(input())
for i in range(1, n+1):
    r = str(i)
    r = r.replace('3', '-').replace('6', '-').replace('9', '-')
    if '-' in r:
        print("-" * r.count('-'), end=" ")
    else:
        print(r, end=" ")
