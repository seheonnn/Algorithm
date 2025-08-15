import heapq


def bfs(n, m, x, y, r, c, k):
    path = ""
    d = ['l', 'r', 'u', 'd']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    pq = []
    heapq.heappush(pq, (path, x, y, 0))

    while pq:
        path, x, y, dist = heapq.heappop(pq)  # dist : 현재까지 이동 거리

        dist_rest = abs(r - x) + abs(c - y)  # 남은 거리

        # 이동 가능 거리 - 현재까지 이동한 거리 < 남은 거리이면 도달 불가능
        # k - 현재까지 이동한 거리 - 남은 거리 (목적지까지의 거리보다 k가 큰 경우) > 0이면 짝수여야 함. 헛이동 후 돌아오기 위함
        if k - dist < dist_rest or (k - dist - dist_rest) % 2 != 0: continue

        if dist == k and x == r and y == c:
            return path

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or n < nx or ny < 1 or m < ny: continue

            heapq.heappush(pq, (path + d[i], nx, ny, dist + 1))

    return "impossible"  # return 값 이용 or answer를 list로 만들어서 answer[0] = path로 넘겨도 됨. 리스트는 mutable

def solution(n, m, x, y, r, c, k):
    return bfs(n, m, x, y, r, c, k)