from day07.node import Node


class Dir(Node):
    _children: dict[str, Node]
    _cached_size: int | None

    def __init__(self, parent: 'Node' = None) -> None:
        super().__init__(parent)
        self._children = dict()
        self._cached_size = None

    def get_size(self) -> int:
        if self._cached_size is None:
            self._cached_size = sum([child.get_size() for child in self._children.values()])
        return self._cached_size
    
    def add_child(self, name: str, child: Node) -> None:
        self._children[name] = child
    
    def get_child(self, name: str) -> Node:
        return self._children[name]
    
    def clear_cached_sizes(self) -> None:
        self._cached_size = None
        [dir.clear_cached_sizes() for dir in self.get_subdirs(False)]

    def get_subdirs(self, recursive: bool = True) -> list['Dir']:
        if recursive:
            return sum([[node] + node.get_subdirs() for node in self._children.values() if type(node) is Dir], [])
        else:
            return sum([[node] for node in self._children.values() if type(node) is Dir], [])