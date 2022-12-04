from base_solver import BaseSolver

class Day3Solver(BaseSolver):

    def item_priority(self, item: chr) -> int:
        if item >= 'a' and item <= 'z':
            return ord(item) - ord('a') + 1
        return ord(item) - ord('A') + 27

    def iter_intersection(self, iters: iter) -> iter:
        result = iters[0]
        for i in iters[1:]:
            result = [x for x in result if x in i]
        return result

    def puzzle1(self) -> str:
        rucksacks = self.get_raw_input()
        priority_total = 0
        for rucksack in rucksacks:
            compartment_length = len(rucksack)//2
            compartments = [rucksack[:(compartment_length)],rucksack[compartment_length:]]
            priority_total += self.item_priority(self.iter_intersection(compartments)[0])
        return str(priority_total)

    def puzzle2(self) -> str:
        rucksacks = self.get_raw_input()
        priority_total = 0
        for i in range(0, len(rucksacks), 3):
            priority_total += self.item_priority(self.iter_intersection(rucksacks[i:i+3])[0])
        return str(priority_total)