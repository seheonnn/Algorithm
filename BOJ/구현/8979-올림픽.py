import sys
input = sys.stdin.readline

n, k = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]

country.sort(key=lambda x : (x[1],x[2],x[3]), reverse=True) # 내림차순

idx = [i for i in range(n) if country[i][0] == k][0] # k 국가의 인덱스 찾기

for i in range(n): # 모든 국가를 확인
    if country[idx][1:] == country[i][1:]: # k국가와 같은 메달수라면 같은 등수임 (동점이거나 본인인 경우)
        print(i+1)
        break
