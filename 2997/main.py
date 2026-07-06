"""six sept"""
RA = int(input())
RB = int(input())
esWinner = input()
if esWinner == "A":
    ea = 1/ (1+10**((RB - RA)/400))
    print(f"{ea:.2f}")
else:
    eb = 1/ (1+10**((RA - RB)/400))
    print(f"{eb:.2f}")
