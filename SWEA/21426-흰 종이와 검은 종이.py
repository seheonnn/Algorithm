# 흰 종이와 겹치는 곳의 넓이 구하는 함수
def get_overlap_area(x1, y1, x2, y2, x3, y3, x4, y4):
    tmp_x1 = max(x1, x3)
    tmp_y1 = max(y1, y3)
    tmp_x2 = min(x2, x4)
    tmp_y2 = min(y2, y4)

    if tmp_x1 < tmp_x2 and tmp_y1 < tmp_y2:
        return (tmp_x2 - tmp_x1) * (tmp_y2 - tmp_y1)
    return 0

T = int(input())
for _ in range(T):
    # 흰 종이와 두 검은 종이의 좌표를 입력받음
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    # 흰 종이의 전체 넓이
    white_area = (x2 - x1) * (y2 - y1)

    # 흰 종이와 첫 번째 검은 종이의 겹치는 넓이
    overlap1 = get_overlap_area(x1, y1, x2, y2, x3, y3, x4, y4)
    # 흰 종이와 두 번째 검은 종이의 겹치는 넓이
    overlap2 = get_overlap_area(x1, y1, x2, y2, x5, y5, x6, y6)

    # 첫 번째 검은 종이와 두 번째 검은 종이의 겹치는 넓이 중 흰 종이와 겹치는 부분만 고려 (overlap1, 2가 흰 종이와 검은 종이의 겹치는 부분만 계산하였기 때문)
    overlap_both = get_overlap_area(x1, y1, x2, y2,
                                          max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))

    # 최종적으로 흰 종이의 보이는 영역 계산
    visible_white = white_area - (overlap1 + overlap2 - overlap_both)

    # 흰 종이의 보이는 영역이 남아있는지 여부 출력
    if visible_white > 0:
        print("YES")
    else:
        print("NO")
