from day07.node import Node


class File(Node):
    _size: int

    def __init__(self, size: int) -> None:
        super().__init__()
        self._size = size
    
    def get_size(self) -> int:
        return self._size