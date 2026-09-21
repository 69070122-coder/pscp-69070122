'''box'''
w,l,m,n = map(int, input().split())
answer = w * l
for a in range(m, n + 1):
    waste = (w % a) * (l % a)
    answer = min(answer, waste)
print(answer)
