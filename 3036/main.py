'''checking the shortest path from curtain input to 1'''
import math
N = int(input())

row = math.isqrt(N-1) + 1 #find the row of n
location = N - (row-1)**2 #find location in row

if location % 2 == 1:
    print(f"{2 * (row - 1)}")
else:
    print(f"{2 * (row - 1) - 1}")
