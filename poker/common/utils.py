from poker.common.models.card import Card
from poker.common.models.game_state import GameState


def print_cards(cards: list[Card], end='\n'):
    for card in cards:
        print(card, end=" ")
    print(end)

def print_info_from_game(game_state: GameState, end='\n'):
    print(f'Current player is: {game_state.current_player.name}')
    print(f'Pot = {game_state.pot}')
    print(f'Bet = {game_state.bet}')
    print('Turned cards in this round are: ')
    print_cards(game_state.turned_cards)

def print_initial_game_info(game_state: GameState, end='\n'):
    print('Basic information about restrictions related to bets, raise and player order are: ')
    print('Player order is: ')
    for play in game_state.player_order:
        print(play.name, end=" ")
    print(end)
    print(f'Small Blind Bet is {game_state.game.small_blind_bet} \n'
          f'Big Blind Bet is {game_state.game.big_blind_bet} \n'
          f'Minimum raise multiplier is {game_state.game.min_raise_multiplier} \n'
          f'Maximum raise multiplier is {game_state.game.max_raise_multiplier}')
    print(end)