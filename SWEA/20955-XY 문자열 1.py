T = int(input())
for t in range(1, T + 1):
    s = input()
    e = input()

    n = len(e)
    while len(e) > len(s):
        if e[-1] == 'X':
            e = e[:-1] # 마지막 문자 삭제
        elif e[-1] == 'Y':
            e = e[:-1]
            e = e[::-1]
        else:
            break

    if e == s:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")

# 3
# Y
# XYYX
# XY
# XYY
# X
# YY