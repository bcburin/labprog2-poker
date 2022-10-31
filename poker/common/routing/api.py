from poker.common.routing.router import Router


class Api(Router):

    def __init__(self, *, name: str):
        super().__init__(prefix=name)
        self._name = name

    @property
    def name(self):
        return self._name
