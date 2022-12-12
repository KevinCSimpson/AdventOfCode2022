from base_solver import BaseSolver
from day09.direction import Direction
from day09.move import Move
from day09.rope import Rope


class Day9Solver(BaseSolver):
    def puzzle1(self) -> str:
        moves = self._get_moves()
        rope = Rope()
        tail_positions = set()
        for move in moves:
            for _ in range(move.count):
                rope.move_head(move.direction)
                tail_positions.add(rope.get_tail())
        return str(len(tail_positions))
    
    def puzzle2(self) -> str:
        moves = self._get_moves()
        rope = Rope(10)
        tail_positions = set()
        for move in moves:
            for _ in range(move.count):
                rope.move_head(move.direction)
                tail_positions.add(rope.get_tail())
        return str(len(tail_positions))

    def _get_moves(self) -> list[Move]:
        raw_moves = self.get_raw_input()
        return [self._get_move(raw_move) for raw_move in raw_moves]

    def _get_move(self, raw_move: str) -> Move:
        raw_parts = raw_move.split(' ')
        match raw_parts[0]:
            case 'U':
                direction = Direction.UP
            case 'D':
                direction = Direction.DOWN
            case 'L':
                direction = Direction.LEFT
            case 'R':
                direction = Direction.RIGHT
        
        return Move(direction, int(raw_parts[1]))