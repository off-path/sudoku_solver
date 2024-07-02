sudoku = ["120070560", "507932080", "000001000", "010240050", "308000402", "070085010", "000700000", "080423701", "034010028"]

# Create matrice
matrice = [[int(char) for char in row] for row in sudoku]

def is_valid(matrice, row, col, num):
    # check row
    if num in matrice[row]:
        return False
    
    # check col
    if num in [matrice[r][col] for r in range(9)]:
        return False
    
    # check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if matrice[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(matrice):
    for row in range(9):
        for col in range(9):
            if matrice[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(matrice, row, col, num):
                        matrice[row][col] = num
                        if solve_sudoku(matrice):
                            return True
                        matrice[row][col] = 0
                return False
    return True

solve_sudoku(matrice)
for row in matrice:
    print("".join(map(str, row)))