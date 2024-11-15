# Greedy - 첫 번째 행만 체크
T = int(input())

for _ in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    expected = [[ i * n + j + 1 for j in range(n)] for i in range(n) ] # 1 기준 : A[i,j]=(i-1) x N + j / 0 기준이므로 i*n+j+1

    cnt = 0 # 전치 연산 횟수

    s = [] # 첫 번째 행의 각 요소가 목표 위치에 있는지
    for i in range(1, n): # 첫 번째 행렬이 정렬되면 나머지도 알아서 정렬됨
        s.append(graph[0][i] == expected[0][i])

    s.reverse() # 우측부터 체크

    state = True

    for i in s: # 제 위치에 있지 않은 경우
        if i != state:
            if state == True:
                state = False
            else:
                state = True
            cnt += 1

    print(cnt)

# 만약 3번 째 숫자가 목표와 다르다면 3x3 행렬에 대해서만 전치