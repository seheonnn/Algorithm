import itertools

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    r = set() # 중복값 제거를 위해 set 사용
    for i in range(1, len(numbers) + 1): # 문자열 길이만큼 수열 생성
        for j in itertools.permutations(list(numbers), i):
            num = int("".join(j))
            r.add(num)
    for num in r:
        if check_prime(num):
            answer += 1
    return answer