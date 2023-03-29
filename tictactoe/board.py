class Board:
    def __init__(self, boardSize) -> None:
        self.boardSize = boardSize
        self.board = [[None] * boardSize for _ in range(boardSize)]
        self.total = self.boardSize**2
        self.currentCount = 0
    
    def checkIfRowWin(self, row, col, piece):
        for crRow in range(len(self.board)):
            if self.board[crRow][col] != piece:
                return False
        
        return True

    def checkIfColWin(self, row, col, piece):
        for crCol in range(len(self.board)):
            if self.board[row][crCol] != piece:
                return False

        return True

    def checkIfDiagonalWin(self, row, col, piece):
        if row != col and row + col != len(self.board)-1:
            return False
        
        firstDiagonalFound = None
        if row == col:
            firstDiagonalFound = True
            for i in range(len(self.board)):
                if self.board[i][i] != piece:
                    firstDiagonalFound = False
                    break
        
        if firstDiagonalFound:
            return True

        secondDiagonalFound = None
        if row + col == len(self.board)-1:
            secondDiagonalFound = True
            for i in range(len(self.board)):
                if self.board[i][self.boardSize-i-1] != piece:
                    secondDiagonalFound = False
                    break

        if secondDiagonalFound == True:
            return True
        
        return False
    
    def checkIfPlayerWins(self, row, col, piece):
        return self.checkIfRowWin(row, col, piece) or self.checkIfColWin(row, col, piece) or self.checkIfDiagonalWin(row, col, piece)

    def isFull(self):
        if self.currentCount == self.total:
            return True
        
        return False

    def IsPosValid(self, row, col):        
        if row  >= self.boardSize or col >= self.boardSize or self.board[row][col]:
            return False
        
        return True

    def markPosition(self, row, col, symbol):
        self.board[row][col] = symbol
        self.currentCount += 1
    

    def __str__(self) -> str:
        s = ""
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                if self.board[row][col]:
                    s += ' ' + str(self.board[row][col])
                
                else:
                    s += ' _ '
            
            s += '\n'
        
        return s
                
