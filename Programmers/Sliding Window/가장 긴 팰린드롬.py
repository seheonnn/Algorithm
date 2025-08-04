def getPaline(s, left, right, n):
    while 0 <= left and right < n and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1 # while 내부가 실행되고 조건이 끝나므로 -1해야

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        answer = max(answer, getPaline(s, i, i, n)) # 홀수 길이
        answer = max(answer, getPaline(s, i, i + 1, n)) # 짝수 길이

    return answer