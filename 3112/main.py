'''cal of the milktea'''

def main():
    '''add up all the cal'''
    bubble, gram = input().split()
    gram = float(gram)

    tea, sweet, cc = input().split()
    sweet = int(sweet)
    cc = float(cc)

    # พลังงานไข่มุก
    if bubble == "H":
        bubble_cal = gram * 5
    elif bubble == "O":
        bubble_cal = gram * 3
    else:
        bubble_cal = gram * 2

    # พลังงานชา
    if tea == "R":#rose
        if sweet == 1:
            tea_cal = 12
        elif sweet == 2:
            tea_cal = 18
        else:
            tea_cal = 25

    elif tea == "T":#taiwan
        if sweet == 1:
            tea_cal = 15
        elif sweet == 2:
            tea_cal = 20
        else:
            tea_cal = 30

    else:  # Macha
        if sweet == 1:
            tea_cal = 10
        elif sweet == 2:
            tea_cal = 15
        else:
            tea_cal = 20
    total = bubble_cal + tea_cal * cc
    if total % 1 == 0:
        print(f"{total:.0f}")
    else:
        print(f"{total}")
main()
