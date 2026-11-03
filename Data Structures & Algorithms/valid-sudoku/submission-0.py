class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Dcol = collections.defaultdict(set)
        Drow = collections.defaultdict(set)
        Dcube = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in Drow[row]) or (board[row][col] in Dcol[col]) or (board[row][col] in Dcube[row//3, col//3]):
                    return False
                Drow[row].add(board[row][col])
                Dcol[col].add(board[row][col])
                Dcube[row//3, col//3].add(board[row][col])
        return True