from poker.common.routing.api import Api
from poker.interface.cards import router as cards_router
from poker.interface.actions import router as actions_router

api = Api(name='interface')

api.add_router(router=cards_router)
api.add_router(router=actions_router)
