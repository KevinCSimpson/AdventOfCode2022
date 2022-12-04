from abc import ABC, abstractmethod


class BaseSolver(ABC):
    input_filename: str

    def __init__(self, input_filename: str):
        self.input_filename = input_filename

    def get_raw_input(self, split_by: str = '\n') -> iter:
        with open(self.input_filename, 'r') as reader:
            raw = reader.read()
        return raw.split(split_by)
    
    @abstractmethod
    def puzzle1(self) -> str:
        pass

    @abstractmethod
    def puzzle2(self) -> str:
        pass