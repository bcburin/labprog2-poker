from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from poker.common.models.card import Card
from poker.common.models.player import Player
from poker.common.enums.role import Role


@dataclass(frozen=True)
class PlayerState:

    player: Player
    cards: list[Card]
    amount: int
    role: Role
    bet: int = 0
    active: bool = True

    def activate(self) -> PlayerState:
        return self.update_state('active', True)

    def deactivate(self) -> PlayerState:
        return self.update_state('active', False)

    def update_amount(self, amount: int) -> PlayerState:
        if amount < 0:
            raise ValueError(f'Negative amount for {self.player.name}: {amount}')
        return self.update_state('amount', amount)

    def update_cards(self, cards: list[Card]) -> PlayerState:
        return self.update_state('cards', cards)

    def update_role(self, role: Role) -> PlayerState:
        return self.update_state('role', role)

    def update_bet(self, bet: int):
        if bet < 0:
            raise ValueError(f'Negative bet for {self.player.name}: {bet}')
        if bet > self.amount:
            raise ValueError(f'Bet for {self.player.name} bigger than available amount')
        return self.update_state('bet', bet)

    def update_state(self, attr: str, val: Any) -> PlayerState:
        return PlayerState(**{**self.__dict__, attr: val})
