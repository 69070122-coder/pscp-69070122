'''เกมสะสมแต้ม'''
score = 0
N = int(input())
for i in range (N):
    A = input()
    if A == "+":
        score += 10
    else:
        score -= 5
print(score)
