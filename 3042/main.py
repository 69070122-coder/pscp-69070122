"""module for checking how many number in range of N to 0 
can be devide by 10"""
N = int(input())
for i in range(N, -1, -1):
    if not i % 10:
        print(i, end=" ")
