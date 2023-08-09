class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        vertical = [["."] * len(board) for _ in range(len(board))]
        square = [[] * len(board) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] != ".":
                    vertical[i][j] = board[j][i]
                if board[i][j] != ".":
                    # square[(i // 3) + (j // 3)].append(board[i][j])
                    if 0 <= i <= 2:  # i//3
                        if 0 <= j <= 2:  # j//3
                            square[0].append(board[i][j])
                        elif 3 <= j <= 5:  # j//3
                            square[1].append(board[i][j])
                        elif 6 <= j <= 8:  # j//3
                            square[2].append(board[i][j])
                    elif 3 <= i <= 5:  # i//3
                        if 0 <= j <= 2:  # j//3
                            square[3].append(board[i][j])
                        elif 3 <= j <= 5:  # j//3
                            square[4].append(board[i][j])
                        elif 6 <= j <= 8:  # j//3
                            square[5].append(board[i][j])
                    elif 6 <= i <= 8:  # i//3
                        if 0 <= j <= 2:  # j//3
                            square[6].append(board[i][j])
                        elif 3 <= j <= 5:  # j//3
                            square[7].append(board[i][j])
                        elif 6 <= j <= 8:  # j//3
                            square[8].append(board[i][j])
                    # 0-2 = 1
                    # 3-5 = 2
                    # 6-8 = 3
        for i in range(len(board)):
            board[i] = list(filter(lambda a: a != ".", board[i]))
            vertical[i] = list(filter(lambda a: a != ".", vertical[i]))
            if len(board[i]) == len(set(board[i])) and len(vertical[i]) == len(set(vertical[i])) and len(
                    square[i]) == len(set(square[i])):
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    print(Solution.isValidSudoku(Solution(), [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                              [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                              [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
                                 )
          )
    print(Solution.isValidSudoku(Solution(), [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                                              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                              [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                              [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
                                 )
          )
