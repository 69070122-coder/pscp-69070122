'''a e i o u -2'''
name = input().lower()
vowel = ['a','e','i','o','u']
count = [0,0,0,0,0]

for ch in name:
    if ch in vowel:
        count[vowel.index(ch)] += 1

for j in range(5):#me sara 5
    if count[j] > 0:
        print(vowel[j], ":", count[j])
