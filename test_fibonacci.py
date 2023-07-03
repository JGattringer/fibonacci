"""for the test work had to take out the input from user and change it for a parameter called iterator.
had to add it to the __init__ function,  changing from just (self) for (self, iterator), in the end of the program
 you can add the number of iterations that you want for the pytest run it"""

import pytest
class Fibonacci:
    def __init__(self, iterator):
        self.before = 0
        self.next = 1
        self.iterator = iterator

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator <= 0:
            print("Operation is ended")
            raise StopIteration

        sequence = []
        for _ in range(self.iterator):
            sequence.append(self.before)
            self.before, self.next = self.next, self.before + self.next

        self.iterator = 0
        return sequence

class Test_Fibonacci:
    def generate():
        generator = Fibonacci()
        sequence = iter(generator)
        test = {k + 1: v for k, v in enumerate(next(sequence))}
        return test

def test_fibonacci_sequence():
    iterator = 10  # Define the number of iterations desired for the test run
    generator = Fibonacci(iterator)
    sequence = iter(generator)
    result = next(sequence)
    assert len(result) == iterator

pytest