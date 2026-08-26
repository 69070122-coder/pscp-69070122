'''playing card'''
def main():
    '''main'''
    card = input().strip().upper()
    
    # แยกส่วนแต้มและสัญออกจากกัน
    # สัญลักษณ์คือตัวอักษรตัวสุดท้าย ส่วนแต้มคือส่วนที่เหลือ
    suit_char = card[-1]
    rank_str = card[:-1]
    
    rank_name = {
        'A': 'ace',
        'J': 'jack',
        'Q': 'queen',
        'K': 'king'
    }
    
    suit_name = {
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades',
        'C': 'clubs'
    }
    
    # หาชื่อของแต้มไพ่
    if rank_str in rank_name:
        rank = rank_name[rank_str]
    else:
        rank = rank_str  # เป็นตัวเลข 2-10 ใช้ค่าตามที่รับมาได้เลย
    suit = suit_name[suit_char]
    print(f"{rank} of {suit}")

main()
