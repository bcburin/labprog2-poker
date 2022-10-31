

class Player:

    def __init__(self, id: int, name: str | None = None):
        self._id = id
        self._name = name if name else f'Player {self._id}'

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.id == other.id

    def __hash__(self):
        return self.id.__hash__()
