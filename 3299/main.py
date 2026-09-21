'''flower pot'''
l, n = map(int, input().split())
band = 1
while (band * l) * (band * l + 1) // 2 < n:
    band += 1
print(band)
