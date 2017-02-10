class NQueen:
    
            #  0    1    2    3
    board = [[".", ".", ".", "."], # 0
            [ ".", ".", ".", "."], # 1
            [ ".", ".", ".", "."], # 2
            [ ".", ".", ".", "."]] # 3
            
    N = 4
    
    def __init__(self):
        pass
    
    def nQueenBackTrack(self, row, n):
        for i in range(n):
            if self.isTheQueenSafe(row , i):
                print(row,i)
                self.board[row][i] = "Q"
                self.print_the_board()
                if row == n-2:
                    self.print_the_board()
                else:
                    self.nQueenBackTrack(row + 1, n)
    
    def isTheQueenSafe(self, row,col):
        for i in range(self.N):
            # check horizontal Queens
            if self.does_board_has_a_queen_at(row,i) or self.does_board_has_a_queen_at(i, col):
                return False
            # check diagonal Queens Top Left to Bottom right
            mod = self.get_minimum(row,col) - 1
            d_i = row - mod
            d_j = col - mod
            while d_i < self.N and d_j < self.N:
                if self.does_board_has_a_queen_at(d_i, d_j):
                    return False
                d_i = d_i + 1
                d_j = d_j + 1
            # check diagonal Queens Top Right to Bottom Left
            d_ii = row - mod
            d_jj = col + mod
            while d_ii < self.N and d_jj >= 0:
                if self.does_board_has_a_queen_at(d_ii, d_jj):
                    return False
                d_ii = d_ii + 1
                d_jj = d_jj - 1
        return True
    
    def does_board_has_a_queen_at(self,row,col):
        return self.board[row][col] == 'Q'
    
    
    def get_minimum(self,x,y):
        if x < y: 
            return x
        else:
            return y

    def print_the_board(self):
        for val in self.board:
            print (val, "\n")

## test client 
q = NQueen()
q.nQueenBackTrack(0,4)