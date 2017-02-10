class NQueen:
    
    board = None      
    N = 0
    
    def __init__(self, board, N):
        self.board = board
        self.N = N
    
    def nQueenBackTrack(self, row, n):
        for i in range(n):
            if self.isTheQueenSafe(row , i):
                print(row,i)
                self.board[row][i] = "Q"
                #self.print_the_board()
                if row == n - 1:
                    self.print_the_board()
                else:
                    self.nQueenBackTrack(row + 1, n)
                self.board[row][i] = "."
    
    def isTheQueenSafe(self, row,col):
        for i in range(self.N):
                    # check horizontal Queens
                    if self.does_board_has_a_queen_at(row,i) or self.does_board_has_a_queen_at(i, col):
                        return False
                    # check diagonal Queens
                    s = row + col
                    k = row - col
                    for x in range(self.N):
                        for y in range(self.N):
                            if x + y == s and self.board[x][y] == "Q":
                                return False
                            if x - y == k and self.board[x][y] == "Q":
                                return False        
        return True
    
    def does_board_has_a_queen_at(self,row,col):
        try:
            return self.board[row][col] == 'Q'
        except:
            return False
    

    def print_the_board(self):
        for val in self.board:
            print (val, "\n")

## test client 
        #  0    1    2    3
board = [[".", ".", ".", "."], # 0
        [ ".", ".", ".", "."], # 1
        [ ".", ".", ".", "."], # 2
        [ ".", ".", ".", "."]] # 3

#q = NQueen(board, 4)
#q.nQueenBackTrack(0,4)

        #  0    1    2    3   4   5   6   7  
boardB =[[".", ".", ".", ".",".",".",".","."], # 0
        [ ".", ".", ".", ".",".",".",".","."], # 1
        [ ".", ".", ".", ".",".",".",".","."], # 2
        [ ".", ".", ".", ".",".",".",".","."], # 3
        [ ".", ".", ".", ".",".",".",".","."], # 4
        [ ".", ".", ".", ".",".",".",".","."], # 5
        [ ".", ".", ".", ".",".",".",".","."], # 6
        [ ".", ".", ".", ".",".",".",".","."],] # 7

#q = NQueen(boardB, 8)
#q.nQueenBackTrack(0,8)

        #  0    1    2    3   4   5   6   7   8
boardC =[[".", ".", ".", ".",".",".",".",".","."], # 0
        [ ".", ".", ".", ".",".",".",".",".","."], # 1
        [ ".", ".", ".", ".",".",".",".",".","."], # 2
        [ ".", ".", ".", ".",".",".",".",".","."], # 3
        [ ".", ".", ".", ".",".",".",".",".","."], # 4
        [ ".", ".", ".", ".",".",".",".",".","."], # 5
        [ ".", ".", ".", ".",".",".",".",".","."], # 6
        [ ".", ".", ".", ".",".",".",".",".","."], # 7
        [ ".", ".", ".", ".",".",".",".",".","."],]# 8


q = NQueen(boardC, 9)
q.nQueenBackTrack(0,9)