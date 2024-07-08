# 구현 - 크로아티아 알파벳

import sys

s = sys.stdin.readline().strip()
cAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cAlpha:
    s = s.replace(i, '_')

print(len(s))

