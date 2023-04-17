# 달팽이는 올라가고 싶다
A, B, V = map(int, input().split()) # A 올라가고 B 미끄러지고 V: 나무 길이

# Ad - B(d-1) = V
# Ad - Bd + B = V
# d = (V - B) / (A-B)
d = (V - B) / (A - B)
if d == int(d):
    print(int(d))
else:
    print(int(d)+1)