from base_solver import BaseSolver


class Day6Solver(BaseSolver):

    def puzzle1(self) -> str:
        raw = self.get_raw_input()[0]
        return self._find_marker_pos(4, raw)
    
    def puzzle2(self) -> str:
        raw = self.get_raw_input()[0]
        return self._find_marker_pos(14, raw)
    
    def _find_marker_pos(self, marker_length: int, raw: str):
        for pos in range(len(raw) - marker_length):
            if len(set(raw[pos:pos + marker_length])) == marker_length:
                return str(pos + marker_length)
        raise RuntimeError('No marker found.')
