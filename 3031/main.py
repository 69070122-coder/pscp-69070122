'''for calculating how much time do each house have until got swallow by the inl'''
import math
S, N = map(int,input().split())
PI = 3.1416
for i in range(N):
    x, y = map(int,input().split())
    time =math.ceil (PI * (x*x + y*y) / S)
    print(time)
    i += 1
