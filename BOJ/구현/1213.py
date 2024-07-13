# 구현 - 팰린드롬 만들기

import sys

s = sys.stdin.readline().strip()
dic = {}

for c in s:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

cnt = 0
result = ''
mid = ''
for k, v in dic.items(): # key, value 출력
    if v % 2 == 1:
        cnt += 1
        mid = k
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            sys.exit()

for k in sorted(dic.keys()):
    v = dic[k]
    result += (k * (v // 2))

print(result + mid + result[::-1])
