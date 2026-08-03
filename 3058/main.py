'''brick bridge'''
A = int(input())
B = int(input())
goal =int(input())

big = min(B , goal // 5)
remain = goal - (big * 5)

if remain <= A:
    print(min(A,remain))
else:
    print(-1)
