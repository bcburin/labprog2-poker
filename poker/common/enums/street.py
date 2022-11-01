from enum import Enum
from functools import total_ordering


@total_ordering
class Street(Enum):

    PRE_FLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4

    def __le__(self, other):
        if not isinstance(other, Street):
            raise ValueError(f'Cannot compare types Street and {type(other)}')
        return self.value < other.value

    def __eq__(self, other):
        if not isinstance(other, Street):
            return False
        return self.value == other.value

