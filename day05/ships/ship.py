from abc import ABC, abstractmethod
from day05.move import Move


class Ship(ABC):
    _stacks: dict[str, list[str]]
    _crane: list[str] | None

    def __init__(self, stacks: list[list[str]]) -> None:
        self._stacks = stacks
        self._crane = None

    @abstractmethod
    def apply_move(self, move: Move) -> None:
        pass
    
    @abstractmethod
    def _pick_up(self, stack: str) -> None:
        pass
    
    def _drop(self, stack: str) -> None:
        if self._crane is None:
            raise RuntimeError('Crane is not holding a crate.')
        self._stacks[stack] += self._crane
        self._crane = None
    
    def get_stacks(self) -> dict[str, list[str]]:
        return self._stacks