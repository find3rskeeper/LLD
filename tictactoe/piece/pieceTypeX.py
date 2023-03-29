from piece.pieceType import PIECETYPE
from piece.piece import Piece
class PieceTypeX(Piece):
    def __init__(self) -> None:
        super().__init__(PIECETYPE.PIECE_TYPE_X)
    
    def __str__(self) -> str:
        return 'X'
    