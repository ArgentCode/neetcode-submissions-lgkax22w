class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # condition 1
        # for row in board:
        #     vals = []
        #     for val in row:
        #         if val == ".": continue
        #         if val in vals: return False
        #         vals.append(val)
        # # condition 2
        # for col in range(9):
        #     vals = []
        #     for row in range(9):
        #         val = board[row][col]
        #         if val == ".": continue
        #         if val in vals: return False
        #         vals.append(val)
        #     # print(vals)
        # condition 3
        vals = []
        iter = 0
        row_vals = [[], [], [], [], [], [], [], [], []]
        col_vals = [[], [], [], [], [], [], [], [], []]
        for row_bot in [0, 3, 6]:
            for col_bot in [0, 3, 6]:
                square_vals = []
                for row in range(row_bot, row_bot+3):
                    for col in range(col_bot,col_bot+3):
                        val = board[row][col]
                        if val == ".": continue
                        if val in row_vals[row]: return False
                        if val in col_vals[col]: return False
                        if val in square_vals: return False
                        square_vals.append(val)
                        col_vals[col].append(val)
                        row_vals[row].append(val)
        print(iter)
        return True