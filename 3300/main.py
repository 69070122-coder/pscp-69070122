'''good work good life'''
n = int(input())
long = 0
for i in range(n):
    h = int(input())
    if h > 18:
        long += 1
short = n - long
answer = n + max(0, long - short - 1)
print(answer)
