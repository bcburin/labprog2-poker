from __future__ import annotations

from enum import Enum


class Action(Enum):

    CALL = 'Call'
    RAISE = 'Raise'
    FOLD = 'Fold'
    CHECK = 'Check'
    BET = 'Bet'

    @classmethod
    def get_actions(cls, is_preflop: bool = False, is_blind: bool = False, can_check: bool = False) -> list[Action]:
        if is_preflop and is_blind:
            return [Action.BET]
        actions = [cls.CALL, cls.RAISE, cls.FOLD]
        if can_check:
            actions.append(cls.CHECK)
        return actions
