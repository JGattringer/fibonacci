class Fibonacci:
    def __init__(self):
        self.before = 0
        self.next = 1
        self.iterator = int(input("Type the number of characters that you wish to perform the Fibonacci sequence! "))

    def __iter__(self):
        return self

    def __next__(self):
        self.sequencia_fibonacci = self.before
        if self.iterator <= 0:
            print("Operation is ended")
            raise StopIteration
        self.sequencia_fibonacci = []
        for i in range(0, self.iterator - 1):
            self.sum = self.before + self.next
            self.before = self.next
            self.next = self.sum
            self.sequencia_fibonacci.append(self.next)
        return self.sequencia_fibonacci

class Test_Fibonacci:
    def generate():
        generator = Fibonacci()
        sequence = iter(generator)
        test = {k: v for k, v in enumerate(next(sequence))}
        return test

print(Test_Fibonacci.generate())