from typing import Iterable

from poker.common.enums.rank import CardRank
from poker.common.enums.suit import CardSuit
from poker.common.models.card import Card


class Deck:

    @staticmethod
    def iterate_full_deck() -> Iterable[Card]:
        for suit in CardSuit.suits():
            for rank in CardRank.ranks():
                yield Card(rank=rank, suit=suit)
