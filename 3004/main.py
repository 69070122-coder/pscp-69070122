"""67"""
import math
x1,y1,z1 =list(map(int, input().split()))
x2,y2,z2 =list(map(int, input().split()))
d = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(f"{d:.2f}")
