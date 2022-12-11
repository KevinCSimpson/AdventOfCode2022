from abc import ABC, abstractmethod


class Node(ABC):
    _parent: 'Node'

    def __init__(self, parent: 'Node' = None) -> None:
        super().__init__()
        self._parent = parent

    def get_parent(self) -> 'Node':
        if self._parent is None:
            raise RuntimeError('Node has no parent.')
        return self._parent

    @abstractmethod
    def get_size(self) -> int:
        pass