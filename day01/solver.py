from base_solver import BaseSolver

class Day1Solver(BaseSolver):

    def puzzle1(self) -> str:
        calorieTotals = self.get_elf_calories(self.get_raw_input('\n\n'))
        calorieTotals.sort(reverse=True)
        return str(calorieTotals[0])

    def puzzle2(self) -> str:
        calorieTotals = self.get_elf_calories(self.get_raw_input('\n\n'))
        calorieTotals.sort(reverse=True)
        return str(sum(calorieTotals[:3]))

    def get_elf_calories(self, elves: iter) -> iter:
        return [self.sum_calories(elf.split('\n')) for elf in elves]
    
    def sum_calories(self, snacks: iter) -> int:
        return sum([int(x) for x in snacks])