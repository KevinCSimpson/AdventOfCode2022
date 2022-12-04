from base_solver import BaseSolver

class Day1Solver(BaseSolver):

    def puzzle1(self) -> str:
        return ''

    def puzzle2(self) -> str:
        elves = self.get_raw_input('\n\n')
        calorieTotals = []
        for elf in elves:
            calorieTotal = 0
            snacks = elf.split('\n')
            for snack in snacks:
                calorieTotal = calorieTotal + int(snack)
            calorieTotals.append(calorieTotal)
        calorieTotals.sort(reverse = True)
        return str(calorieTotals[0] + calorieTotals[1] + calorieTotals[2])
