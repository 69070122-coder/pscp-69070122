'''pod that are hard to understand'''
N,K = map(int,input().split())
count = [0] * K

for i in range(N):
    kon = int(input())
    count[kon - 1] += 1
    i += 0

trip = min(count)
remain = 0

for j in count:
    remain += j - trip
print(remain)
