from asyncio import run

from poker.interface.api import api


async def show_all_cards():
    await api.do_task('interface.card.show_all_cards', message='These are the available cards')


if __name__ == '__main__':
    run(show_all_cards())

