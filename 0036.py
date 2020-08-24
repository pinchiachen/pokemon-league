## 2020/08/24

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_row_valid(board) and self.is_column_valid(board) and self.is_nine_cell_valid(board)

    def is_row_valid(self, board):
        for row in range(9):
            exist_dict = dict()
            for column in range(9):
                if board[row][column] != '.':
                    if board[row][column] in exist_dict:
                        return False
                    else:
                        exist_dict[board[row][column]] = 1
        return True

    def is_column_valid(self, board):
        for column in range(9):
            exist_dict = dict()
            for row in range(9):
                if board[row][column] != '.':
                    if board[row][column] in exist_dict:
                        return False
                    else:
                        exist_dict[board[row][column]] = 1
        return True

    def is_nine_cell_valid(self, board):
        for i in range(3):
            for j in range(3):
                exist_dict = dict()
                for row in range(3 * i, 3 * (i + 1)):
                    for column in range(3 * j, 3 * (j + 1)):
                        if board[row][column] != '.':
                            if board[row][column] in exist_dict:
                                return False
                            else:
                                exist_dict[board[row][column]] = 1
        return True