from dataclasses import dataclass


@dataclass(frozen=True)
class Player:

    id: int
    name: str | None = None

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.id == other.id

    def __hash__(self):
        return self.id.__hash__()
