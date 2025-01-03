import sys
input = sys.stdin.readline

n, k = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]

country.sort(key=lambda x : (x[1],x[2],x[3]), reverse=True) # 람다 주의 !

k_idx = [i for i in range(n) if country[i][0] == k][0] # k의 인덱스 찾기

for i in range(n):
    if country[k_idx][1:] == country[i][1:]: # k와 메달수가 같다면 같은 등수임
        print(i + 1)
        break