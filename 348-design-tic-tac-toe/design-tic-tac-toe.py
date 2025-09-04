class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.antiDiag = 0
        self.winner = 0

    def move(self, row: int, col: int, player: int) -> int:
        if self.winner: # 0 is considered False
            return self.winner
        point = 1 if player == 1 else -1

        # update rows
        self.rows[row] += point
        self.cols[col] += point

        # update diagonal
        if row == col:
            self.diag += point
        
        # update anti diagonal
        if row + col == self.size - 1:
            self.antiDiag += point
        
        if (abs(self.rows[row]) == self.size or
        abs(self.cols[col]) == self.size or
        abs(self.diag) == self.size or
        abs(self.antiDiag) == self.size):
            self.winner = player

        return self.winner

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
"""
Plan: 
variables:
- rows: list
- cols: list
- board size: int
- diag: int
- anti-diag: int
- winner

Player 1 is 1 and player 2 is -1

validator:
each row/col/diag/anti-diag accumulates a signed total
if that signed total equates to player, that player is the winner
"""