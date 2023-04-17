list = list(map(int,input().split()))
if list == sorted(list):
    print("ascending")
elif list == sorted(list, reverse=True):
    print("descending")
else:
    print("mixed")


# sorted(), sort() 함수 차이.
# sort()는 반환값 없고 원본 list가 수정되어 있음.
# sorted()는 정렬된 값 반환, 원본 유지