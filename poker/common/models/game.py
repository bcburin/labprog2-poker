from dataclasses import dataclass


@dataclass(frozen=True)
class Game:
    small_blind_bet: int
    big_blind_bet: int
    min_raise_multiplier: float
    max_raise_multiplier: float
