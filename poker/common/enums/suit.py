from __future__ import annotations
from enum import Enum
from functools import total_ordering


@total_ordering
class CardSuit(Enum):
    """
    Models a card suit: hearts, diamonds, clubs and spades.

    Supports comparison operators, which check for value equality and compare suit priorities.
    """

    # The values below define the priority
    # The higher the value, the higher the priority
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

    def __le__(self, other):
        if not isinstance(other, CardSuit):
            raise ValueError(f'Cannot compare types CardSuit and {type(other)}')
        return self.value < other.value

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        if not isinstance(other, CardSuit):
            return False
        return self.value == other.value

    def __str__(self):
        match self.value:
            case self.HEARTS:
                return 'H'
            case self.DIAMONDS:
                return 'D'
            case self.CLUBS:
                return 'C'
            case self.SPADES:
                return 'S'

    @classmethod
    def suits(cls) -> list[CardSuit]:
        suit_list = [cls.HEARTS, cls.DIAMONDS, cls.CLUBS, cls.SPADES]
        return sorted(suit_list, key=lambda suit: suit.value)


if __name__ == '__main__':
    s1 = CardSuit.CLUBS
    s2 = CardSuit.HEARTS

    print(s1 < s2)
    print(s1 > s2)
