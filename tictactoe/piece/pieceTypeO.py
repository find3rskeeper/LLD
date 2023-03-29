from piece.pieceType import PIECETYPE
from piece.piece import Piece
class PieceTypeO(Piece):
    def __init__(self) -> None:
        super().__init__(PIECETYPE.PIECE_TYPE_O)
    
    def __str__(self) -> str:
        return 'O'
    