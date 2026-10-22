'''main'''
n = int(input())

for _ in range(n):
    text = input()

    if "baka" in text:
        print("no")
        continue

    text = text.replace("bakka", "")
    text = text.replace("ka", "")
    text = text.replace("ba", "")
    text = text.replace("ta", "")

    if not text:
        print("yes")
    else:
        print("no")
