from __future__ import annotations

from typing import Iterable
import random

from poker.common.enums.rank import CardRank
from poker.common.enums.suit import CardSuit
from poker.common.models.card import Card


class Deck:

    def __init__(self, cards: list[Card], shuffle: bool = True):
        self._cards = random.shuffle(cards) if shuffle else cards

    @property
    def cards(self):
        return self._cards

    def shuffled(self) -> Deck:
        return Deck(cards=self._cards, shuffle=True)

    @staticmethod
    def iterate_full_deck() -> Iterable[Card]:
        for suit in CardSuit.suits():
            for rank in CardRank.ranks():
                yield Card(rank=rank, suit=suit)

    @staticmethod
    def get_full_deck(shuffle: bool = True) -> Deck:
        cards = list(Deck.iterate_full_deck())
        return Deck(cards=cards, shuffle=shuffle)
