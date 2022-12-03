from shape import Shape


class Round(object):
    opponent_shape = Shape.ROCK
    my_shape = Shape.PAPER

    def __init__(self, opponent_shape: Shape, my_shape: Shape):
        self.opponent_shape = opponent_shape
        self.my_shape = my_shape
    
    def __shape_score(self)-> int:
        match self.my_shape:
            case Shape.ROCK:
                return 1
            case Shape.PAPER:
                return 2
            case Shape.SCISSORS:
                return 3
    
    def __outcome_score(self)-> int:
        if self.opponent_shape == self.my_shape:
            return 3
        if self.opponent_shape == Shape.ROCK and self.my_shape == Shape.PAPER:
            return 6
        if self.opponent_shape == Shape.PAPER and self.my_shape == Shape.SCISSORS:
            return 6
        if self.opponent_shape == Shape.SCISSORS and self.my_shape == Shape.ROCK:
            return 6
        return 0
    
    def score(self) -> int:
        return self.__shape_score() + self.__outcome_score()