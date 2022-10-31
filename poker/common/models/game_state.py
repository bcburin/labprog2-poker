from dataclasses import dataclass

from poker.common.enums.street import Street
from poker.common.models.player import Player
from poker.common.models.player_state import PlayerState


@dataclass(frozen=True)
class GameState:

    player_states: dict[Player, PlayerState]
    pot: int
    bet: int
    street: Street

    def get_state_of(self, player: Player) -> PlayerState:
        return self.player_states[player]
