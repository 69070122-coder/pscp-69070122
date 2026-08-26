'''max of the highest value without list'''
N = int(input())
equation = ""
total = 0
if N == 0:
    print("0 = 0")
else:
    for i in range (N):
        X = int(input())
        Y = int(input())
        if X <= Y:
            total += Y
            if i != 0:
                equation += " + "
            equation += str(Y)
        else:
            total += X
            if i != 0:
                equation += " + "
            equation += str(X)

    if N == 1:
        print(equation)
    else:
        print(f"{equation} = {total}")
