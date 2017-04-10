"""
Tell if the queen captures the king.

Input.
Queen position
King position

Positions are encoded as a5, g2 etc.

Output.
"same rank", "same file", "same diagonal" or "king is safe"
"""
    
def file_letter_to_num(s):
    return  ord(s[0]) - ord('a') + 1  # +1 - start from 1, ord trasfer symbol into integer


def position_to_numbers(p):
    """
    Converts position, such as "a1", to numbers, such as (1, 1)
    """
    return (file_letter_to_num(p[0]), int(p[1]))


def check_queen_and_king(queen, king):
    if queen[1] == king[1]:
        return "same rank"
    elif queen[0] == king[0]:
        return "same file"
    queen_numbers = position_to_numbers(queen)
    king_numbers = position_to_numbers(king)
    if (queen_numbers[0] - queen_numbers[1] == 
        king_numbers[0] - king_numbers[1]) or (
        queen_numbers[0] + queen_numbers[1] == 
        king_numbers[0] + king_numbers[1]):
        return "same diagonal"
    else: 
        return "king is safe"


def main():
    with open("chess_in.txt") as f:
        queen = f.readline()[:2]
        king = f.readline()[:2]
        print check_queen_and_king(queen, king)


if __name__ == "__main__":
    main()
