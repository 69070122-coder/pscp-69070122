'''lect or right arrow'''
direc = input()
star = int(input())

def right_arrow():
    '''right'''
    for i in range (star):
        print(" "* (2*i) +"*"*(star-i))
    for i in range (star - 1):
        print(" "* ((2 * star - 4)-(i*2)) + "*" * (i +2))

def left_arrow():
    '''left'''
    for i in range (star):
        print(" " * ((star - 1)-i) + "*" * (star -i))
    for i in range (star -1):
        print(" " * (i + 1) + "*" *(i + 2))

def main():
    '''main'''
    for i in range(len(direc)):
        if direc[i] == "R":
            right_arrow()
        elif direc[i] == "L":
            left_arrow()
        if i != len(direc) -1:
            print("")

main()
