def solution(friends, gifts):
    answer = 0
    n = len(friends)
    pair = [[0] * n for _ in range(n)]
    give = [0] * n
    recv = [0] * n
    friend = {name: i for i, name in enumerate(friends)}
    print(friend)

    for gift in gifts:
        a, b = gift.split()
        i, j = friend[a], friend[b]
        pair[i][j] += 1
        give[i] += 1
        recv[j] += 1

    next_recv = [0] * n
    score = [give[i] - recv[i] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if pair[i][j] > pair[j][i]:
                next_recv[i] += 1
            elif pair[i][j] == pair[j][i]:
                if score[i] > score[j]:
                    next_recv[i] += 1

    return max(next_recv) if next_recv else 0