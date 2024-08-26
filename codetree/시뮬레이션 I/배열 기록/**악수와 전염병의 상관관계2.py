import sys
input = sys.stdin.readline

n, k, p, t = map(int, input().split())
handshakes = [list(map(int, input().split())) for _ in range(t)]

infected = [0] * (n+1) # 감염 여부
remain_transmission = [0] * (n+1) # 전염 가능 횟수

infected[p] = 1 # p 번째 개발자 초기 감염
remain_transmission[p] = k

for t1, x, y in sorted(handshakes, key=lambda x: x[0]): # 각 요소의 첫 번째 값 (시간)을 기준으로 정렬
    # x나 y가 감염되어 있고, 전염 가능한 악수 횟수가 남아 있다면
    if (infected[x] and remain_transmission[x] > 0) or (infected[y] and remain_transmission[y] > 0):
        if not infected[x]: # x가 감염되지 않았다면
            infected[x] = 1
            remain_transmission[x] = k
        else:
            remain_transmission[x] -= 1

        if not infected[y]: # y가 감염되지 않았다면
            infected[y] = 1
            remain_transmission[y] = k
        else:
            remain_transmission[y] -= 1
for lst in infected[1:]:
    print(lst,end="")
# print("".join(map(str, infected[1:])))
