import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
r = sys.maxsize

def dfs(v, idx): # v : 현재까지 스타트 팀에 포함된 사람 수, idx : 다음에 고려할 사람의 인덱스
    global r
    if v == n // 2:
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1: # visited가 1이면 스타트 팀
                    a += graph[i][j]
                elif visited[i] == 0 and visited[j] == 0: # visited가 0이면 링크 팀
                    b += graph[i][j]
        r = min(r, abs(a - b))
        return
    for i in range(idx, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(v + 1, i + 1)
            visited[i] = 0 # 재귀 호출 이후에는 원래 상태로 되돌려 다른 조합을 탐색
dfs(0, 0)
print(r)