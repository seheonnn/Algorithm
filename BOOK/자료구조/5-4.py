def recursive_function(i):
    # 100번째 호출시 종료되도록
    if i == 100:
        return
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i + 1)
    print(i, "번째 재귀 함수를 종료합니다.")

recursive_function(1)