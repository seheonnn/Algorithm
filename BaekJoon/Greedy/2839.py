# N킬로그램 배달해야 할 때, 5kg, 3kg 총 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오
import sys
N = int(sys.stdin.readline())
cnt = 0
while N >= 0:
    if N % 5 == 0:
        cnt += (N//5)
        print(cnt)
        break
    N -= 3 # 5의 배수가 될 때까지 -3
    cnt += 1
else:
    print(-1)
