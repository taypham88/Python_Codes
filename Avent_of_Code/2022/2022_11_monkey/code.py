#--- Advent of code 2022 ---
#--- Day 11: Monkey in the Middle ---

class Monkey:
    def __init__(self, name: int, worryLevels : list, operation: list, test: int):
        self.name = name
        self.worryLevels = worryLevels
        self.operation = operation
        self.test = test
for i in range(10):
    print(i, i//3, i//3 + bool(i%3))

