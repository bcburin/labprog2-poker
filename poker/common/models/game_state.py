from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from poker.common.enums.street import Street
from poker.common.models.card import Card
from poker.common.models.deck import Deck
from poker.common.models.game import Game
from poker.common.models.player import Player
from poker.common.models.player_state import PlayerState


@dataclass(frozen=True)
class GameState:

    game: Game
    player_states: dict[Player, PlayerState]
    player_order: list[Player]
    current_player: Player
    pot: int = 0
    bet: int = 0
    street: Street = Street.PRE_FLOP
    start_of_street: bool = True
    player_can_check: bool = False
    deck: Deck = Deck.get_full_deck()
    turned_cards: list[Card] = field(default_factory=list)

    @property
    def last_player(self) -> Player | None:
        if self.start_of_street:
            return None
        for i, player in enumerate(self.player_order):
            if player == self.current_player:
                return self.player_order[i-1] if i != 0 else self.player_order[-1]

    @property
    def next_player(self) -> Player:
        current_index = self.player_order.index(self.current_player)
        return self.player_order[(current_index + 1) % len(self.player_order)]

    @property
    def players(self) -> list[Player]:
        return self.player_order

    def get_state_of(self, player: Player) -> PlayerState:
        return self.player_states[player]

    def update_deck(self, cards: list[Card], shuffle: bool = True) -> GameState:
        return self.update_state('deck', Deck(cards=cards, shuffle=shuffle))

    def update_turned_cards(self, cards: list[Card]) -> GameState:
        return self.update_state('turned_cards', cards)

    def update_state(self, attr: str, val: Any) -> GameState:
        return GameState(**{**self.__dict__, attr: val})
