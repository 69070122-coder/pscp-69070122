'''this module is for change the tem. unit'''
temp = float(input())
unit_1 = input()
unit_2 = input()
def temp_to_c():
    '''this function is for changing the user unit to celceus for further use'''
    if unit_1 == "C":
        new_temp = temp
    elif unit_1 == "K":
        new_temp = temp - 273.15
    elif unit_1 == "F":
        new_temp = (temp - 32) / 1.8
    else:
        new_temp = (temp / 1.8) - 273.15
    return new_temp

def main():
    '''this function for calculate from c to the temp thaat user want'''
    new_temp = temp_to_c()
    if unit_2 == "K":
        final_temp = new_temp + 273.15
    elif unit_2 == "F":
        final_temp = (new_temp * 1.8 ) + 32
    elif unit_2 =="R":
        final_temp = (new_temp + 273.15) * 1.8
    else:
        final_temp = new_temp
    print(f"{final_temp:.2f}")

main()
