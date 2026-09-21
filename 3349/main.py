'''charm'''
n = int(input())
count = [0] * 301
for i in range(n):
    bowl = int(input())
    count[bowl] += 1
print(max(count))
