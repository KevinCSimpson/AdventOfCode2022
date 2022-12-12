from day09.direction import Direction


class Rope(object):
    _knots: list[tuple[int, int]]

    def __init__(self, knot_count: int = 2) -> None:
        self._knots = [(0, 0) for _ in range(knot_count)]
    
    def move_head(self, direction: Direction):
        match direction:
            case Direction.UP:
                self._knots[0] = (self._knots[0][0], self._knots[0][1] + 1)
            case Direction.DOWN:
                self._knots[0] = (self._knots[0][0], self._knots[0][1] - 1)
            case Direction.LEFT:
                self._knots[0] = (self._knots[0][0] - 1, self._knots[0][1])
            case Direction.RIGHT:
                self._knots[0] = (self._knots[0][0] + 1, self._knots[0][1])
        self._update_tail()
        return

    def get_tail(self) -> tuple[int, int]:
        return self._knots[len(self._knots) - 1]
    
    def _update_tail(self) -> None:
        for idx, knot in enumerate(self._knots[1:], 1):
            self._knots[idx] = self._follow_knot(knot, self._knots[idx - 1])

    def _follow_knot(self, this_knot: tuple[int, int], knot_to_follow: tuple[int, int]) -> tuple[int, int]:
        delta = self._sub_pos(knot_to_follow, this_knot)
        new_knot = this_knot
        if abs(delta[0]) <= 1 and abs(delta[1]) <= 1:
            return new_knot
        match delta:
            case (2, 0):
                new_knot = self._add_pos(this_knot, (1, 0))
            case (-2, 0):
                new_knot = self._add_pos(this_knot, (-1, 0))
            case (0, -2):
                new_knot = self._add_pos(this_knot, (0, -1))
            case (0, 2):
                new_knot = self._add_pos(this_knot, (0, 1))
            case (2,2) | (2, 1) | (1, 2):
                new_knot = self._add_pos(this_knot, (1, 1))
            case (-2, 2) | (-2, 1) | (-1, 2):
                new_knot = self._add_pos(this_knot, (-1, 1))
            case (-2, -2) | (-2, -1) | (-1, -2):
                new_knot = self._add_pos(this_knot, (-1, -1))
            case (2, -2) | (2, -1) | (1, -2):
                new_knot = self._add_pos(this_knot, (1, -1))
            case _:
                raise RuntimeError('Rope lost its tail.')
        return new_knot
    
    def _add_pos(self, first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
        return (first[0] + second[0], first[1] + second[1])
    
    def _sub_pos(self, first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
        return self._add_pos(first, (-1 * second[0], -1 * second[1]))