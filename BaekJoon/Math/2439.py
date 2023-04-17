# reverse 별찍기
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i)+"*"*i)


# print() 뒤에 줄바꿈 없애려면 print("", end="")