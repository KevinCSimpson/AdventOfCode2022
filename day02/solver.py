from outcome import Outcome
from shape import Shape
from round import Round


def build_round(opponent_shape: Shape, desired_outcome: Outcome) -> Round:
    match desired_outcome:
        case Outcome.DRAW:
            my_shape = opponent_shape
        case Outcome.WIN:
            match opponent_shape:
                case Shape.ROCK:
                    my_shape = Shape.PAPER
                case Shape.PAPER:
                    my_shape = Shape.SCISSORS
                case Shape.SCISSORS:
                    my_shape = Shape.ROCK
        case Outcome.LOSE:
            match opponent_shape:
                case Shape.ROCK:
                    my_shape = Shape.SCISSORS
                case Shape.PAPER:
                    my_shape = Shape.ROCK
                case Shape.SCISSORS:
                    my_shape = Shape.PAPER

    return Round(opponent_shape, my_shape)


with open('day02\input.txt','r') as reader:
    raw = reader.read()
rounds_raw = raw.split('\n')
total_score = 0
for round_raw in rounds_raw:
    round_shapes_raw = round_raw.split(' ')
    match round_shapes_raw[0]:
        case 'A':
            opponent_shape = Shape.ROCK
        case 'B':
            opponent_shape = Shape.PAPER
        case 'C':
            opponent_shape = Shape.SCISSORS
    
    match round_shapes_raw[1]:
        case 'X':
            desired_outcome = Outcome.LOSE
        case 'Y':
            desired_outcome = Outcome.DRAW
        case 'Z':
            desired_outcome = Outcome.WIN
    
    round = build_round(opponent_shape, desired_outcome)
    total_score += round.score()
print(total_score)


