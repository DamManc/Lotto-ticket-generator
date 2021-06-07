import random


class Bill:
    id = 1

    def __init__(self, play_type, numbers, city, money_bet):
        self.id = Bill.id
        self.play_type = play_type
        self.numbers = []
        self.money_bet = money_bet
        while len(self.numbers) < numbers:
            number = random.randint(1, 90)
            if number not in self.numbers:
                self.numbers.append(number)
        self.city = city
        Bill.id += 1

    def __str__(self):
        return f'+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*50}+{"-"*10}+\n' \
               f'|{"BILL_ID".center(10)}|{"PLAY".center(10)}|{"MONEY_BET".center(10)}|{"NUMBERS".center(50)}|{"CITY".center(10)}|\n' \
               f'+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*50}+{"-"*10}+\n' \
               f'|{str(self.id).center(10)}|{self.play_type.center(10)}|{str(self.money_bet).center(10)}|{"".join(str(self.numbers)).center(50)}|{self.city.center(10)}|\n' \
               f'+{"-"*10}+{"-"*10}+{"-"*10}+{"-"*50}+{"-"*10}+\n'




