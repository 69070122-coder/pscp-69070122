'''how many vowel again'''
N = int((input()))
alphabeth = []
vowel = ['A','E','I','O','U']
count = 0
for i in range(N):
    alphabeth.append(input().capitalize())

for i in alphabeth:
    if i in vowel:
        count += 1
print(count)
