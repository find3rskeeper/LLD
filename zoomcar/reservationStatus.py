from enum import Enum, auto

class RESERVATIONSTATUS(Enum):
    SCHEDULED = auto()
    INPROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()
