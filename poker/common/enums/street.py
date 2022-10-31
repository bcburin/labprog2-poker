from enum import Enum
from functools import total_ordering


@total_ordering
class Street(Enum):

    PRE_FLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4

    def __le__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

