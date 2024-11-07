import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lst.append((x1, x2))
ans = []
r = 0

def overlapped(seg1, seg2):
    (ax1, ax2), (bx1, bx2) = seg1, seg2

    # 두 선분이 겹치는지 여부는
    # 한 점이 다른 선분에 포함되는 경우로 판단 가능합니다.
    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
           (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)

def possible():
    num_segs = len(ans)
    for i in range(num_segs):
        seg1 = ans[i]
        for j in range(i + 1, num_segs):
            seg2 = ans[j]
            if overlapped(seg1, seg2):
                return False  # 겹치는 선분이 발견되면 False 반환
    return True  # 모든 선분이 겹치지 않으면 True 반환

def choose(curr_num):
    global r
    if curr_num == n:
        if possible():
            r = max(r, len(ans))
        return
    ans.append(lst[curr_num])
    choose(curr_num + 1)
    ans.pop()

    choose(curr_num + 1)
choose(0)
print(r)