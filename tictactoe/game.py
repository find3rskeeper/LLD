from player import Player
from queue import Queue
from board import Board
from piece import pieceTypeO, pieceTypeX
class Game:
    def __init__(self, boardSize, players) -> None:
        self.q = Queue()
        self.board = Board(boardSize)
        self.symbols = Queue()
        for symbol in [pieceTypeO.PieceTypeO(), pieceTypeX.PieceTypeX()]:
            self.symbols.put(symbol)

        for name in players:
            playerPeice = self.provideRandomSymbol()
            player = Player(name, playerPeice)
            self.q.put(player)
    
    def provideRandomSymbol(self):
        symbol = self.symbols.get()
        return symbol

            

    def play(self):
        while True:
            row, col = input('Enter position for player {} '.format(self.q.queue[0].name)).split()
            row, col = int(row), int(col)
            if not self.board.IsPosValid(row, col):
                print('Invalid Input')
                continue
            
            
            player = self.q.get()
            self.board.markPosition(row, col, player.piece)
            print(str(self.board))

            if self.board.checkIfPlayerWins(row, col, player.piece):
                print('Player {} Won'.format(player.name))
                break
            
            if self.board.isFull():
                print('Its a tie')
                break

            self.q.put(player)
            