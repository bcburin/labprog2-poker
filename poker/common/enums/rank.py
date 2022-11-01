from __future__ import annotations
from enum import Enum
from functools import total_ordering


@total_ordering
class CardRank(Enum):

    # Ace
    ACE = 10

    # Regular numbers
    TWO = 20
    THREE = 30
    FOUR = 40
    FIVE = 50
    SIX = 60
    SEVEN = 70
    EIGHT = 80
    NINE = 90
    TEN = 100

    # Court Cards
    JACK = 110
    QUEEN = 120
    KING = 130

    # Aliases
    A = ACE
    J = JACK
    Q = QUEEN
    K = KING

    def __le__(self, other):
        if not isinstance(other, CardRank):
            raise ValueError(f'Cannot compare types CardRank and {type(other)}')
        return self.value < other.value

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        if not isinstance(other, CardRank):
            return False
        return self.value == other.value

    def __str__(self):
        match self.value:
            case self.ACE:
                return 'A'
            case self.TWO:
                return '2'
            case self.THREE:
                return '3'
            case self.FOUR:
                return '4'
            case self.FIVE:
                return '5'
            case self.SIX:
                return '6'
            case self.SEVEN:
                return '7'
            case self.EIGHT:
                return '8'
            case self.NINE:
                return '9'
            case self.TEN:
                return '10'
            case self.J:
                return 'J'
            case self.Q:
                return 'Q'
            case self.K:
                return 'K'

    @classmethod
    def ranks(cls) -> list[CardRank]:
        rank_list = [
            cls.A, cls.TWO, cls.THREE, cls.FOUR, cls.FIVE, cls.SIX,
            cls.SEVEN, cls.EIGHT, cls.NINE, cls.TEN, cls.J, cls.Q, cls.K
        ]
        return sorted(rank_list, key=lambda rank: rank.value)
