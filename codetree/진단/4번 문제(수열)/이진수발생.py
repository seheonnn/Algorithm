import sys
input = sys.stdin.readline

def gen(s, n, result):
    if len(s) == n:
        result.append(s)
        return
    if s == '' or s[-1] == '1': # 한 글자에 대한 s[-1]는 오류 발생
        gen(s + '0', n, result)
    gen(s + '1', n, result)

n = int(input().strip())
result = []
gen('', n, result)

result.sort()  # 결과를 사전순으로 정렬
for binary in result:
    print(binary)
