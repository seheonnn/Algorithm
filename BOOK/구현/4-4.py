# 구현 - 왕실의 나이트

def sol():
    i = input()
    column = ord(i[0]) - 97 + 1 # 'a' : 97
    row = int(i[1])

    steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    result = 0
    for i in steps:
        nc = column + i[0]
        nr = row + i[1]

        if nr < 1 or nc < 1 or nr > 8 or nc > 8:
            continue
        result += 1

    print(result)

def ans():
    return

sol()
