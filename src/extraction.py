import random


class Extraction:
    counter = 0

    def __init__(self, city, numbers=5):
        self.city = city
        self.numbers = []
        while len(self.numbers) < numbers:
            number = random.randint(1, 90)
            if number not in self.numbers:
                self.numbers.append(number)

    def __str__(self):
        return f'+{"-" * 10}+{"-" * 50}+\n|{self.city.center(10)}|{"".join(str(self.numbers)).center(50)}|\n+{"-" * 10}+{"-" * 50}+\n'
