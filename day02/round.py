from day02.outcome import Outcome
from day02.shape import Shape


class Round(object):
    opponent_shape: Shape
    my_shape: Shape
    outcome: Outcome 

    wins = [[Shape.ROCK, Shape.PAPER], [Shape.PAPER, Shape.SCISSORS], [Shape.SCISSORS, Shape.ROCK]]

    def __init__(self, opponent_shape: Shape = None, my_shape: Shape = None, outcome: Outcome = None):
        if len([x for x in [opponent_shape, my_shape, outcome] if x is None]) != 1:
            raise Exception("Must provide exactly two of {opponent_shape, my_shape, outcome}.")

        if opponent_shape is None:
            match outcome:
                case Outcome.LOSE:
                    self.opponent_shape = [x[1] for x in self.wins if x[0] == my_shape][0]
                case Outcome.DRAW:
                    self.opponent_shape = my_shape
                case Outcome.WIN:
                    self.opponent_shape = [x[0] for x in self.wins if x[1] == my_shape][0]
        else:
            self.opponent_shape = opponent_shape
        
        if my_shape is None:
            match outcome:
                case Outcome.LOSE:
                    self.my_shape = [x[0] for x in self.wins if x[1] == opponent_shape][0]
                case Outcome.DRAW:
                    self.my_shape = opponent_shape
                case Outcome.WIN:
                    self.my_shape = [x[1] for x in self.wins if x[0] == opponent_shape][0]
        else:
            self.my_shape = my_shape

        if outcome is None:
            if opponent_shape == my_shape:
                self.outcome = Outcome.DRAW
            else:
                if len([x for x in self.wins if x[0] == opponent_shape and x[1] == my_shape]) > 0:
                    self.outcome = Outcome.WIN
                else:
                    self.outcome = Outcome.LOSE
        else:
            self.outcome = outcome
    
    def __shape_score(self)-> int:
        match self.my_shape:
            case Shape.ROCK:
                return 1
            case Shape.PAPER:
                return 2
            case Shape.SCISSORS:
                return 3
    
    def __outcome_score(self)-> int:
        match self.outcome:
            case Outcome.LOSE:
                return 0
            case Outcome.DRAW:
                return 3
            case Outcome.WIN:
                return 6
    
    def score(self) -> int:
        return self.__shape_score() + self.__outcome_score()