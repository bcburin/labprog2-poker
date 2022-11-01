from poker.common.enums.role import Role
from poker.common.enums.street import Street
from poker.common.models.game_state import GameState
from poker.common.routing.router import Router


router = Router(prefix='actions')


@router.add('small_blind_bet')
def bet(game_state: GameState):
    current_player_state = game_state.player_states[game_state.current_player]
    current_player_role = current_player_state.role
    if current_player_role != Role.SMALL_BLIND:
        raise ValueError('Current player is not Small Blind')
    if game_state.street != Street.PRE_FLOP:
        raise ValueError('Small Blind only bets in the fist street (PRE-FLOP)')
    new_player_state = current_player_state.update_bet(game_state.game.small_blind_bet)
