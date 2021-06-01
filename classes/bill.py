import random


class Bill:
    counter = 0

    def __init__(self, play_type, numbers, city):
        self.play_type = play_type
        self.numbers = [random.randint(1, 90) for i in range(numbers)]
        self.city = city
        Bill.counter += 1

    def __str__(self):
        return f'+{"-"*10}+{"-"*50}+{"-"*10}+\n|{"PLAY".center(10)}|{"NUMBERS".center(50)}|{"CITY".center(10)}|\n+{"-"*10}+{"-"*50}+{"-"*10}+\n|{self.play_type.center(10)}|{"".join(str(self.numbers)).center(50)}|{self.city.center(10)}|\n+{"-"*10}+{"-"*50}+{"-"*10}+\n'




