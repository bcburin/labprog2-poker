from asyncio import run

from poker.common.enums.role import Role
from poker.common.enums.street import Street
from poker.common.models.deck import Deck
from poker.common.models.game import Game
from poker.common.models.game_state import GameState
from poker.common.models.player import Player
from poker.common.models.player_state import PlayerState
from poker.interface.api import api


async def test_show_all_cards():
    await api.do_task('interface.card.show_all_cards', message='These are the available cards')


async def test_ask_for_player_action():
    game = Game(small_blind_bet=10, big_blind_bet=20, min_raise_multiplier=2, max_raise_multiplier=2)
    player = Player(id=0)
    cards = list(Deck.iterate_full_deck())[0:2]
    player_state = PlayerState(player=player, cards=cards, amount=1000, role=Role.BIG_BLIND)
    game_state = GameState(
        player_states={player: player_state},
        player_order=[player],
        current_player=player,
        street=Street.FLOP,
        pot=500, bet=150,
        player_can_check=True,
        game=game
    )
    action, amount = await api.do_task('interface.action.ask_for_player_action', game_state=game_state)
    print(f'Chose action: {action} {amount if amount else ""}')


if __name__ == '__main__':
    # run(test_show_all_cards())
    run(test_ask_for_player_action())
