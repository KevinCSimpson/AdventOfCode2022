from base_solver import BaseSolver


class Day4Solver(BaseSolver):

    def raw_pair_to_ranges(self, raw: str) -> iter:
        elves_raw = raw.split(',')
        range_limits_raw = [x.split('-') for x in elves_raw]
        return [range(int(x[0]), int(x[1]) + 1) for x in range_limits_raw]

    def puzzle1(self) -> str:
        pairs_raw = self.get_raw_input()
        pair_ranges = [self.raw_pair_to_ranges(x) for x in pairs_raw]
        return str(len([x for x in pair_ranges if len(set(x[0]).union(set(x[1]))) == max(len(x[0]), len(x[1]))]))

    def puzzle2(self) -> str:
        pairs_raw = self.get_raw_input()
        pair_ranges = [self.raw_pair_to_ranges(x) for x in pairs_raw]
        return str(len([x for x in pair_ranges if len(set(x[0]).union(set(x[1]))) != len(x[0]) + len(x[1])]))