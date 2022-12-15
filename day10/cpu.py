from day10.instruction import Instruction
from day10.instruction_type import InstructionType


class Cpu(object):
    register_x: int
    _instruction: Instruction
    _timer: int

    def __init__(self) -> None:
        self.register_x = 1
        self._instruction = None
        self._timer = 0
    
    def tick(self) -> None:
        self._timer -= 1
        if self._timer > 0:
            return
        match self._instruction.instruction_type:
            case InstructionType.ADDX:
                self.register_x += self._instruction.param
        self._instruction = None

    def is_ready_for_instruction(self) -> bool:
        return self._instruction is None

    def send_instruction(self, instruction: Instruction) -> None:
        self._instruction = instruction
        match instruction.instruction_type:
            case InstructionType.NOOP:
                self._timer = 1
            case InstructionType.ADDX:
                self._timer = 2