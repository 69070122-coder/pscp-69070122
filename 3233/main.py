'''salak kin bang'''
result = input().split()
buy = input().split()

win_letter = result[0]
win_number = result[1]

buy_letter = buy[0]
buy_number = buy[1]

if win_letter == buy_letter and win_number == buy_number:
    prize = 1000000
elif win_number == buy_number:
    prize = 100000
elif win_letter == buy_letter and win_number[-3:] == buy_number[-3:]:
    prize = 2000
elif win_letter == buy_letter and win_number[-2:] == buy_number[-2:]:
    prize = 1000
elif win_letter != buy_letter and win_number[-3:] == buy_number[-3:]:
    prize = 200
elif win_letter != buy_letter and win_number[-2:] == buy_number[-2:]:
    prize = 100
elif win_letter == buy_letter:
    prize = 20
else:
    prize = 0

print(prize)
