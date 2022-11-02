from poker.common.models.card import Card


def print_cards(cards: list[Card], end='\n'):
    for card in cards:
        print(card, end=" ")
    print(end)
