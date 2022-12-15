from base_solver import BaseSolver
from day10.cpu import Cpu
from day10.instruction import Instruction
from day10.instruction_type import InstructionType


class Day10Solver(BaseSolver):
    def puzzle1(self) -> str:
        cpu = Cpu()
        program = self.get_program()
        ptr = 0
        cycle = 0
        interesting_cycles = [x for x in range(20, 221, 40)]
        signal_strength_sum = 0
        while ptr < len(program):
            cycle += 1
            if cycle in interesting_cycles:
                signal_strength_sum += cpu.register_x * cycle
            if cpu.is_ready_for_instruction():
                cpu.send_instruction(program[ptr])
                ptr += 1
            cpu.tick()
        
        return str(signal_strength_sum)

    def puzzle2(self) -> str:
        cpu = Cpu()
        program = self.get_program()
        ptr = 0
        cycle = 0
        crt = [' ' for x in range(240)]
        while ptr < len(program):
            cycle += 1

            register_x = cpu.register_x
            if (cycle - 1) % 40 in range(register_x - 1, register_x + 2):
                crt[cycle - 1] = '#'
            else:
                crt[cycle - 1] = '.'

            if cpu.is_ready_for_instruction():
                cpu.send_instruction(program[ptr])
                ptr += 1
            cpu.tick()
        
        return '\n' + ''.join([''.join(crt[x:x+40]) + '\n' for x in range(0, 241, 40)])
    
    def get_program(self) -> list[Instruction]:
        raw = self.get_raw_input()
        return [self.get_instruction(x) for x in raw]
    
    def get_instruction(self, raw: str) -> Instruction:
        parts = raw.split(' ')
        match parts[0]:
            case 'noop':
                return Instruction(InstructionType.NOOP)
            case 'addx':
                return Instruction(InstructionType.ADDX, int(parts[1]))