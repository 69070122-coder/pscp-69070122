'''main'''
W, H, M, N = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
widths = []
last = 0
for x in X:
    widths.append(x - last)
    last = x
widths.append(W - last)
heights = []
last = 0
for y in Y:
    heights.append(y - last)
    last = y
heights.append(H - last)
widths.sort(reverse=True)
heights.sort(reverse=True)
a = widths[0] * heights[0]
b = widths[0] * heights[1]
c = widths[1] * heights[0]
d = widths[1] * heights[1]
areas = [a, b, c, d]
areas.sort(reverse=True)
print(areas[0], areas[1])
