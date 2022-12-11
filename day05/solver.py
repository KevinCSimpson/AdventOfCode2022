import re
from base_solver import BaseSolver
from day05.move import Move
from day05.ships.ship import Ship
from day05.ships.ship9000 import Ship9000
from day05.ships.ship9001 import Ship9001


class Day5Solver(BaseSolver):
    _move_regex: re.Pattern

    def __init__(self, input_filename: str):
        super().__init__(input_filename)
        self._move_regex = re.compile('^move (?P<count>\d+) from (?P<start>\w+) to (?P<end>\w+)$')

    def puzzle1(self):
        raw = self.get_raw_input('\n\n')
        stacks = self.get_stacks(raw[0])
        ship = Ship9000(stacks)
        moves = self.get_moves(raw[1])
        for move in moves:
            ship.apply_move(move)
        return self.get_tops_of_stacks(ship.get_stacks())

    def puzzle2(self):
        raw = self.get_raw_input('\n\n')
        stacks = self.get_stacks(raw[0])
        ship = Ship9001(stacks)
        moves = self.get_moves(raw[1])
        for move in moves:
            ship.apply_move(move)
        return self.get_tops_of_stacks(ship.get_stacks())

    def get_stacks(self, raw: str) -> Ship:
        raw_rows = raw.split('\n')
        raw_labels = raw_rows.pop()
        labels = raw_labels.split()
        stacks = {label: list() for label in labels}
        for raw_row in (list(r) for r in raw_rows):
            for idx, crate_label in enumerate(raw_row[1::4]):
                if crate_label != ' ':
                    stacks[labels[idx]].insert(0, crate_label)
        return stacks
    
    def get_moves(self, raw: str) -> list[Move]:
        moves = list()
        for raw_row in raw.split('\n'):
            m = self._move_regex.match(raw_row)
            moves.append(Move(int(m.group('count')), m.group('start'), m.group('end')))
        return moves
    
    def get_tops_of_stacks(self, stacks:  dict[str, list[str]]) -> str:
        return ''.join([stack[-1] for stack in stacks.values()])