from day09.direction import Direction


class Move(object):
    direction: Direction
    count: int

    def __init__(self, direction: Direction, count: int) -> None:
        self.direction = direction
        self.count = count