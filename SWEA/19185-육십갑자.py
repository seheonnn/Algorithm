TC = int(input())

for tc in range(1, TC + 1):
    r = []
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    q = int(input())
    for _ in range(q):
        y = int(input())

        idx1 = (y - 1) % len(s) # y번째 년도가 리스트 s에서 몇 번째 문자열에 해당하는지
        idx2 = (y - 1) % len(t)

        r.append(s[idx1]+t[idx2]) # 해당 년도의 이름 생성하여 결과 리스트에 추가

    print(f"#{tc}", " ".join(r))
    # print("#" + str(tc), end=" ")
    # for el in r:
    #     print(el, end=" ")
