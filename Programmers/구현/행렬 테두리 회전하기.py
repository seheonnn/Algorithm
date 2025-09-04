def solution(rows, columns, queries):
    answer = []

    matrix = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        cur = matrix[x1][y1]
        min_cur = cur

        # 위쪽 행 : 왼 -> 오
        for y in range(y1 + 1, y2 + 1):
            matrix[x1][y], cur = cur, matrix[x1][y]
            min_cur = min(min_cur, cur)

        # 오른쪽 열 : 위 -> 아래
        for x in range(x1 + 1, x2 + 1):
            matrix[x][y2], cur = cur, matrix[x][y2]
            min_cur = min(min_cur, cur)

        # 아래 행 : 오 -> 왼
        for y in range(y2 - 1, y1 - 1, -1):
            matrix[x2][y], cur = cur, matrix[x2][y]
            min_cur = min(min_cur, cur)

        # 왼쪽 열 : 아래 -> 위
        for x in range(x2 - 1, x1 - 1, -1):
            matrix[x][y1], cur = cur, matrix[x][y1]
            min_cur = min(min_cur, cur)

        answer.append(min_cur)

    return answer