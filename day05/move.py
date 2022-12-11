class Move(object):
    count: int
    start: str
    end: str

    def __init__(self, count: int, start: str, end: str) -> None:
        self.count = count
        self.start = start
        self.end = end