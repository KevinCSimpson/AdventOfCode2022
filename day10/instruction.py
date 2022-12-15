from day10.instruction_type import InstructionType


class Instruction(object):
    instruction_type: InstructionType
    param: int

    def __init__(self, instruction_type: InstructionType, param: int = None) -> None:
        self.instruction_type = instruction_type
        self.param = param