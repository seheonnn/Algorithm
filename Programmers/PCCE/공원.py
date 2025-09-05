def check(mat, park, x, y):
    for i in range(x, x + mat):
        for j in range(y, y + mat):
            if park[i][j] != '-1':
                return False
    return True

def solution(mats, park):
    answer = 0
    n = len(park)
    m = len(park[0])

    mats.sort(reverse=True)
    for mat in mats:
        for i in range(n - mat + 1):
            for j in range(m - mat + 1):
                if check(mat, park, i, j):
                    return mat
    return -1