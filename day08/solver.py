from base_solver import BaseSolver


class Day8Solver(BaseSolver):
    def puzzle1(self) -> str:
        trees = self._get_trees()
        visible_count = sum([sum([1 for row in range(len(trees)) if self._is_tree_visible(row, col, trees)]) for col in range(len(trees[0]))])
        return str(visible_count)
    
    def puzzle2(self) -> str:
        trees = self._get_trees()
        return str(max([max([self._get_tree_scenic_score(row, col, trees) for row in range(len(trees))]) for col in range(len(trees[0]))]))
    
    def _get_trees(self) -> list[list[int]]:
        rows_raw = self.get_raw_input()
        return [[int(tree) for tree in list(row)] for row in rows_raw]
    
    def _is_tree_visible(self, row: int, col: int, trees: list[list[int]]) -> bool:
        tree_height = trees[row][col]
        if all([r[col] < tree_height for r in trees[0:row]]):
            return True
        if all([r[col] < tree_height for r in trees[row + 1:len(trees)]]):
            return True
        if all([c < tree_height for c in trees[row][0:col]]):
            return True
        if all([c < tree_height for c in trees[row][col + 1:len(trees[row])]]):
            return True
        return False
    
    def _get_tree_scenic_score(self, row: int, col: int, trees: list[list[int]]) -> int:
        tree_height = trees[row][col]

        north_score = 0
        for r in range(row - 1, -1, -1):
            north_score += 1
            if trees[r][col] >= tree_height:
                break

        south_score = 0
        for r in range(row + 1, len(trees)):
            south_score += 1
            if trees[r][col] >= tree_height:
                break
        
        east_score = 0
        for c in range(col + 1, len(trees[row])):
            east_score += 1
            if trees[row][c] >= tree_height:
                break
        
        west_score = 0
        for c in range(col - 1, -1, -1):
            west_score += 1
            if trees[row][c] >= tree_height:
                break
        
        return north_score * south_score * east_score * west_score