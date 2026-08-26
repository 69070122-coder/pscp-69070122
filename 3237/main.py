'''piramid'''
N = int(input())
for i in range (N):
    if not i or i == N-1:
        print("0"* (i+1))
    else:
        print("0"+ "1"*(i-1) + "0")
