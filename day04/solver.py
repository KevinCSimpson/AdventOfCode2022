import re
from base_solver import BaseSolver


class Day4Solver(BaseSolver):

    r: re.Pattern

    def __init__(self, input_filename: str) -> None:
        super().__init__(input_filename)
        self.r = re.compile('^(?P<first>\d+)-(?P<second>\d+),(?P<third>\d+)-(?P<fourth>\d+)$')

    def raw_line_to_ranges(self, raw: str) -> iter:
        m = self.r.fullmatch(raw)
        return [range(int(m.group('first')), int(m.group('second')) + 1), range(int(m.group('third')), int(m.group('fourth')) + 1)]

    def parse_raw(self, raw_lines: str) -> iter:
        return [self.raw_line_to_ranges(x) for x in raw_lines]

    def puzzle1(self) -> str:
        pair_ranges = self.parse_raw(self.get_raw_input())
        return str(len([x for x in pair_ranges if len(set(x[0]).union(set(x[1]))) == max(len(x[0]), len(x[1]))]))

    def puzzle2(self) -> str:
        pair_ranges = self.parse_raw(self.get_raw_input())
        return str(len([x for x in pair_ranges if len(set(x[0]).union(set(x[1]))) != len(x[0]) + len(x[1])]))