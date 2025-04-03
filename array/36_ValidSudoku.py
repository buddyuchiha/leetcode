# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.



# Solution 1 (cringe and long)

def colChecker(board):
     pass
def rowChecker(board):
     pass
def x3Checker(board):
     pass
def isValidSudoku(board: list[list[str]]) -> bool:
    for row in board:
        row_str = "".join(row)
        row_str = row_str.replace('.','')
        for num in row_str:
            if row_str.count(num) > 1:
                return False
    for i in range(len(board)):
        b = ''
        for row in board: 
            b += row[i]
        b = b.replace('.','')
        for num in b:
            if b.count(num) > 1:
                return False    
    first = ''
    second = ''
    third = '' 
    counter = 0
    for row in board: 
        string = "".join(row)
        first += string[:3]
        second += string[3:6]
        third += string[6:9]
        counter += 1
        if counter == 3: 
                    first = first.replace('.','')
                    second = second.replace('.','')
                    third = third.replace('.','')
                    for num in first:
                        if first.count(num) > 1:
                            return False
                    for num in second:
                        if second.count(num) > 1:
                            return False
                    for num in third:
                        if third.count(num) > 1:
                            return False
                    first = ''
                    second = ''
                    third = '' 
                    counter = 0
    return True
            
# Solution 2 (shorter and better must be)
def checker(string: list) -> bool:
    """
    Function which help to check column and rows. Making a string and count dublicates
    Params: 
        string (str) - a string which means row or column 
    Returns:
        bool - True if there are not dublicates otherwise False
    """
    result = "".join(string)
    result = result.replace('.','')
    for num in result:
        if result.count(num) > 1:
            return False
    return True

def x3Checker(board) -> bool:
    """
    Function which help to check 3x3 boxes. Making a lot of cycles, check values in 3x3 boxes and compare list and set length
    Params: 
        boatd (list[list[str]]) - sudoku board
    Returns:
        bool - True if there are not dublicates otherwise False
    """
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subboard = []
            for row in range(i, i+3):
                for col in range(j, j+3):
                    value = board[row][col]
                    if value.isdigit():
                        subboard.append(value)
                    else: 
                        continue
            if len(subboard) != len(set(subboard)):
                return False
    return True

                       
def isValidSudoku2(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        b = ''
        for row in board: 
            if not checker(row):
                return False
            b += row[i]
        if not checker(b):
            return False 
    if not x3Checker(board):
        return False
    return True


            
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku2(board))
        