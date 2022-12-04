from base_solver import BaseSolver

class Day1Solver(BaseSolver):

    def puzzle1(self) -> str:
        calorieTotals = self.get_elf_calories_sorted(self.get_raw_input('\n\n'))
        return str(calorieTotals[0])

    def puzzle2(self) -> str:
        calorieTotals = self.get_elf_calories_sorted(self.get_raw_input('\n\n'))
        return str(sum(calorieTotals[:3]))

    def get_elf_calories_sorted(self, elves: iter) -> iter:
        return sorted([self.sum_calories(elf.split('\n')) for elf in elves], reverse=True)
    
    def sum_calories(self, snacks: iter) -> int:
        return sum([int(x) for x in snacks])