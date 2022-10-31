from poker.common.enums.rank import CardRank
from poker.common.enums.suit import CardSuit


class Card:

    def __init__(self, *, rank: CardRank, suit: CardSuit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self) -> CardRank:
        return self._rank

    @property
    def suite(self) -> CardSuit:
        return self._suit

    def __str__(self):
        return f'<{str(self.suite)} {str(self.rank)}>'


