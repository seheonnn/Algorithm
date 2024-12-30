# import sys
# input = sys.stdin.readline
#
# t = int(input())
#
# for _ in range(t):
#     s = list(input().strip())
#
#     score = 0
#     seq = 0
#     for i in range(len(s)):
#         if s[i] == "O":
#             seq += 1
#             score += seq
#         elif s[i] == "X":
#             seq = 0
#     print(score)

import sys
input = sys.stdin.readline

t = int(input())

def func(s, idx, seq, score):
    if idx == len(s):
        return score

    if s[idx] == "O":
        return func(s, idx+1, seq+1, score + seq + 1)
    elif s[idx] == "X":
        return func(s, idx+1, 0, score)

for _ in range(t):
    s = input().strip()
    print(func(s, 0, 0, 0))