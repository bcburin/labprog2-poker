from poker.common.enums.role import Role
from poker.common.enums.action import Action
from poker.common.models.game_state import GameState
from poker.common.models.player_state import PlayerState
from poker.common.routing.router import Router
from poker.common.enums.street import Street

router = Router(prefix='action')


@router.add(route='ask_for_player_action')
def show_possible_actions(
        player_state: PlayerState,
        game_state: GameState
) -> tuple[Action, int | None]:
    actions = Action.get_actions(
        is_preflop=(game_state.street == Street.PRE_FLOP),
        is_blind=(player_state.role == Role.BIG_BLIND or player_state.role == Role.SMALL_BLIND),
        can_check=game_state.player_can_check
    )
    actions_dict = {i: action for i, action in enumerate(actions)}
    for i, action in actions_dict.items():
        print(f'{i} - {action}')
    choice = int(input('Choice: '))
    chosen_action = actions[choice]
    amount = None
    if chosen_action != Action.FOLD and chosen_action != Action.CHECK:
        amount = int(input('Amount: '))
    return chosen_action, amount
