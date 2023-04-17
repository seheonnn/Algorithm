while(1):
    n = input()
    if n=="0":
        break
    # n[::-1]은 n을 뒤집음. n[::1]은 그대로
    if (n==n[::-1]):
        print("yes")
    else:
        print("no")



# while len(str) > 1:
#     if str.pop(0) != str.pop():
#         return False