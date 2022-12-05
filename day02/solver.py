from base_solver import BaseSolver
from day02.outcome import Outcome
from day02.shape import Shape
from day02.round import Round


class Day2Solver(BaseSolver):

    def puzzle1(self) -> str:
        opponent_shape_dict = {
            'A': Shape.ROCK,
            'B': Shape.PAPER,
            'C': Shape.SCISSORS
        }
        my_shape_dict = {
            'X': Shape.ROCK,
            'Y': Shape.PAPER,
            'Z': Shape.SCISSORS
        }
        
        rounds_raw = [x.split(' ') for x in self.get_raw_input()]
        rounds = [Round(opponent_shape=opponent_shape_dict[x[0]], my_shape=my_shape_dict[x[1]]) for x in rounds_raw]
        return str(sum([x.score() for x in rounds]))

    def puzzle2(self) -> str:
        opponent_shape_dict = {
            'A': Shape.ROCK,
            'B': Shape.PAPER,
            'C': Shape.SCISSORS
        }
        outcome_dict = {
            'X': Outcome.LOSE,
            'Y': Outcome.DRAW,
            'Z': Outcome.WIN
        }
        
        rounds_raw = [x.split(' ') for x in self.get_raw_input()]
        rounds = [Round(opponent_shape=opponent_shape_dict[x[0]], outcome=outcome_dict[x[1]]) for x in rounds_raw]
        return str(sum([x.score() for x in rounds]))