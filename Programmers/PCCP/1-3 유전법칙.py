def solution(queries):
    answer = []

    for n, p in queries:
        if n == 1:
            answer.append("Rr")
        else:
            x = p - 1
            div = 4 ** (n - 2)  # 각 세대별 개수
            r = "Rr"
            while div > 0:
                d = (x // div) % 4
                if d == 0:
                    r = "RR"
                    break
                if d == 3:
                    r = "rr"
                    break
                div //= 4
            answer.append(r)
    return answer