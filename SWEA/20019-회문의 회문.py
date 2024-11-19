# T = int(input())
# for t in range(1, T + 1):
#     s = input()
#     if s == s[::-1]:
#         n = len(s)
#         tmp = s[:(n-1) // 2]
#         if tmp == tmp[::-1]:
#             idx = n - ((n - 1)// 2)
#             tmp2 = s[idx:]
#             if tmp2 == tmp2[::-1]:
#                 print("#" + str(t) + " YES")
#             else:
#                 print("#" + str(t) + " NO")
#         else:
#             print("#" + str(t) + " NO")
#     else:
#         print("#" + str(t) + " NO")



def is_palindrome(s):
    return s == s[::-1]

T = int(input())
for t in range(1, T + 1):
    s = input()
    n = len(s)
    # 기존 문자열, # S의 처음 (N−1)/2 길이의 부분, S의 마지막 (N−1)/2 길이의 부분 팰린드롬 체크
    if is_palindrome(s) \
        and is_palindrome(s[:(n-1)//2]) \
            and is_palindrome(s[(n + 1) // 2:]):
        print("#" + str(t) + " YES")
    else:
        print("#" + str(t) + " NO")