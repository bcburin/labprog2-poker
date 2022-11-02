from unittest import TestCase, main

from poker.common.enums.action import Action
from poker.common.enums.role import Role
from poker.common.enums.street import Street
from poker.common.models.deck import Deck
from poker.common.models.game_state import GameState
from poker.common.models.player import Player
from poker.common.models.player_state import PlayerState
from poker.interface.api import api


class TestActionsInInterface(TestCase):

    def test_ask_for_player_action(self):
        # Preparation
        player = Player(id=0)
        cards = list(Deck.iterate_full_deck())[0:2]
        player_state = PlayerState(player=player, cards=cards, amount=1000, role=Role.BIG_BLIND)
        game_state = GameState(
            player_states={player: player_state},
            street=Street.FLOP,
            pot=500, bet=150,
            player_can_check=True
        )
        # Test
        action, amount = await api.do_task(
            'interface.action.ask_for_player_action',
            player_state=player_state,
            game_state=game_state,
        )
        # Assertions
        print(f'Chose action: {action} {amount if amount else ""}')
        if action == Action.FOLD or action == Action.CHECK:
            self.assertIsNone(amount)


if __name__ == '__main__':
    main()
