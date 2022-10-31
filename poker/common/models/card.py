from dataclasses import dataclass

from poker.common.enums.rank import CardRank
from poker.common.enums.suit import CardSuit


@dataclass(frozen=True)
class Card:

    rank: CardRank
    suit: CardSuit

    def __str__(self):
        return f'<{str(self.suit)} {str(self.rank)}>'


