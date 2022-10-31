from poker.common.routing.router import Router
from poker.common.models.deck import Deck


router = Router(prefix='card')


@router.add(route='show_all_cards')
def show_all_cards(message: str | None = None):
    print(message)
    count = 0
    for card in Deck.iterate_full_deck():
        print(card)
        count += 1
    print(f'Total: {count}')
