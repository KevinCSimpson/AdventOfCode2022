from base_solver import BaseSolver
from day07.dir import Dir
from day07.file import File
from day07.terminal_parser import TerminalParser


class Day7Solver(BaseSolver):
    def puzzle1(self) -> str:
        root = TerminalParser.parse(self.get_raw_input())
        dirs = root.get_subdirs() + [root]
        return str(sum([dir.get_size() for dir in dirs if dir.get_size() <= 100000]))

    def puzzle2(self) -> str:
        total_disk_space = 70000000
        required_unused_space = 30000000

        root = TerminalParser.parse(self.get_raw_input())
        dirs = root.get_subdirs() + [root]

        total_used_space = root.get_size()

        return str(min([dir.get_size() for dir in dirs if (total_disk_space - total_used_space) + dir.get_size() >= required_unused_space]))