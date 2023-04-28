# heapq의 기본은 최소힙. 가장 작은 값이 맨 앞에
# -1 곱해줌으로써 최대힙. 가장 큰 값이 맨 앞에
import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, (-1)*x)
