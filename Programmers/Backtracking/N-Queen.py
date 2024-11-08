# def 재귀함수(n):
# 	if 정답이면 :
# 		출력 or 저장
# 	else : 정답이 아니면 :
# 		for 모든 자식 노드에 대해서:
# 			if 정답에 유망하다면(답의 가능성이 있으면) :
# 				자식노드로이동
# 				재귀함수(n+1)
# 				부모노드로 이동

def solution(n): # 마지막 테스트 케이스 시간초과, 백트래킹 템플릿

    def is_safe(board, row, col):
        for i in range(row):
            # 왼쪽 위 대각선, (i, board[i])에 있는 퀸이 (row, col)와 왼쪽 위 대각선에 있다면 board[i] - i == col - row 성립
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row: # 오른쪽 위 대각선
                return False
        return True

    def backtrack(row):
        if row == n: # row 가 n에 도달했다는 것은 퀸이 각 행에 하나씩 배치되었다는 의미
            return 1

        cnt = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col # 퀸을 배치했음을 표시
                cnt += backtrack(row + 1) # 다음 퀸 배치
        return cnt

    board = [-1] * n # 퀸이 놓인 위치를 저장하는 배열. board[0] = 1 은 퀸이 0, 1에 위치한다는 뜻
    return backtrack(0)





# 정답 코드
def solution(n):
    # 세로줄, 왼쪽 대각선, 오른쪽 대각선을 추적하는 집합
    cols = set()
    left_diagonals = set()    # (row - col)로 계산
    right_diagonals = set()   # (row + col)로 계산

    def backtrack(row):
        if row == n:  # 모든 행에 퀸을 배치했다면
            return 1

        cnt = 0
        for col in range(n):
            # 세로줄, 왼쪽 대각선, 오른쪽 대각선에 충돌이 없는 경우
            if col not in cols and (row - col) not in left_diagonals and (row + col) not in right_diagonals:
                # 현재 위치에 퀸을 놓음
                cols.add(col)
                left_diagonals.add(row - col)
                right_diagonals.add(row + col)

                cnt += backtrack(row + 1)  # 다음 행으로 이동

                # 퀸을 제거하고, 다른 위치에 놓기 위해 상태 복원
                cols.remove(col)
                left_diagonals.remove(row - col)
                right_diagonals.remove(row + col)

        return cnt

    return backtrack(0)
