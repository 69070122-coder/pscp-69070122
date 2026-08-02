'''is it increasing or decreasing'''
def main():
    '''main'''
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    if num_1 < num_2 < num_3:
        print("increasing")
    elif num_1 > num_2 > num_3:
        print("decreasing")
    else:
        print("neither")

main()
