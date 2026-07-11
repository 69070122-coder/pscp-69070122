"""salub"""
def main():
    """salub"""
    num = input()
    m = input()
    swap = int(num[::-1])
    if m == "+":
        total = int(num)+swap
    else :
        total = int(num)*swap
    print(f"{num} {m} {swap} = {total}")
main()
