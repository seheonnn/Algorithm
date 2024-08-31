# import sys
# input = sys.stdin.readline

# s = input()
# ln = len(s)
# cnt = 0
# for i in range(1, ln):
#     if s[i] == "(" and s[i-1] == "(":
#         for j in range(i+2, ln):
#             if s[j] == ")" and s[j-1] == ")":
#                 cnt += 1
# print(cnt)

import sys
input = sys.stdin.readline

s = input()
ln = len(s)
cnt = 0
for i in range(ln-1):
        for j in range(i + 1, ln - 1):
            if s[i] == "(" and s[i+1] == "(" and s[j] == ")" and s[j+1] == ")":
                cnt += 1
print(cnt)