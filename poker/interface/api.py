from poker.common.routing.api import Api
from poker.interface.cards import router as cards_router

api = Api(name='interface')

api.add_router(router=cards_router)
