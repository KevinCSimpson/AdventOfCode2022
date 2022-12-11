from day05.move import Move
from day05.ships.ship import Ship


class Ship9000(Ship):

    def apply_move(self, move: Move) -> None:
        for _ in range(move.count):
            self._pick_up(move.start)
            self._drop(move.end)
    
    def _pick_up(self, stack: str) -> None:
        if self._crane is not None:
            raise RuntimeError('Crane is already holding crates.')
        self._crane = [self._stacks[stack].pop()]