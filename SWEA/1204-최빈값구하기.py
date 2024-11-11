T = int(input())
for _ in range(T):
    t = input()
    arr = list(map(int, input().split()))
    dic = {}

    for num in arr:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    most_num = 0
    most_freq = 0
    for num, freq in dic.items():
        if freq > most_freq:
            most_num = num
            most_freq = freq

    print("#"+t, most_num)