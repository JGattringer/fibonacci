class Fibonacci:
    def __init__(self):
        self.before = 0
        self.next = 1
        self.iterator = int(input("Type the number of characters that you wish to perform the Fibonacci sequence! "))

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

print(Test_Fibonacci.generate())