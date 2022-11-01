from poker.common.routing.api import Api
from poker.backend.cards import router as card_router


api = Api(name='backend')


api.add_router(router=card_router)
