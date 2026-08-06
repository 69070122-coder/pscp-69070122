'''big sale'''
import math
A,B,C = map(int,input().split())
if A+B+C >= 3:
    print(math.floor((25*A + 40*B + 55*C)*0.9))
else:
    print(25*A + 40*B + 55*C)
