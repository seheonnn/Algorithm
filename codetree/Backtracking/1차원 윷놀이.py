import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
pieces = [1] * k

ans = 0

# 점수 계산
def calc():
    score = 0
    for piece in pieces:
        score += (piece >= m)
    return score

def find_max(cnt):
    global ans

    # 말을 직접 n번 움직이지 않아도
    # 최대가 될 수 있으므로 항상 답을 갱신
    ans = max(ans, calc())

    # 더 이상 움직일 수 없을 때 종료
    if cnt == n:
        return

    for i in range(k):
        # 움직여도 점수가 그대로라면 더 이상 움직이지 않음
        if pieces[i] >= m:
            continue

        pieces[i] += nums[cnt]
        find_max(cnt + 1)
        pieces[i] -= nums[cnt]

find_max(0)
print(ans)