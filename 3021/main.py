'''this module is for finding if the circle was overlap 
by checking the length between 2 point and the length of 2 rad of the circle'''
import math
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
d = math.sqrt((x1 - x2)**2 + (y1 -y2)**2)
if r1 + r2 >= d:
    print("overlapping")
else:
    print("no overlapping")
