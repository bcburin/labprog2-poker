from poker.common.enums.role import Role
from poker.common.enums.action import Action
from poker.common.models.game_state import GameState
from poker.common.routing.router import Router
from poker.common.enums.street import Street
from poker.common.utils import print_cards, print_info_from_game

router = Router(prefix='action')


@router.add(route='ask_for_player_action')
def ask_for_player_action(
        game_state: GameState
) -> tuple[Action, int | None]:
    player_state = game_state.get_state_of(game_state.current_player)
    actions = Action.get_actions(
        is_preflop=(game_state.street == Street.PRE_FLOP),
        is_blind=(player_state.role == Role.BIG_BLIND or player_state.role == Role.SMALL_BLIND),
        can_check=game_state.player_can_check
    )
    # Show info from game and current player cards
    print_info_from_game(game_state)
    print('Your cards are:')
    print_cards(player_state.cards)
    # Show available actions
    actions_dict = {i + 1: action for i, action in enumerate(actions)}
    for i, action in actions_dict.items():
        print(f'{i} - {action}')
    # Get player input
    choice = int(input('Choice: '))
    chosen_action = actions_dict[choice]
    # Get amount (if applicable)
    amount = None
    if chosen_action != Action.FOLD and chosen_action != Action.CHECK:
        amount = int(input('Amount: '))
    return chosen_action, amount
