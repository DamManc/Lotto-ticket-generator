def check_play_numbers(bill_numbers, bill_play_type, extraction_numbers):
    count_win_numbers = 0
    winner_nums = []
    for bill_n in bill_numbers:
        for ext_n in extraction_numbers:
            if bill_n == ext_n:
                winner_nums.append(bill_n)
                count_win_numbers += 1
    for k in Lotto.TYPE_PLAY:
        if k == bill_play_type and Lotto.TYPE_PLAY[k] == count_win_numbers:
            return winner_nums
    return False


class Lotto:
    TYPE_PLAY = {'estratto': 1, 'ambo': 2, 'terno': 3, 'quaterna': 4, 'cinquina': 5}
    NUMBERS = [n for n in range(1, 11)]
    NAME_CITIES = ['bari', 'cagliari', 'firenze', 'genova', 'roma', 'palermo', 'torino', 'venezia', 'milano', 'napoli']

    def __init__(self, bills, extractions):
        self.bills = bills
        self.extractions = extractions

    def winner_wheels(self):
        # create a dict of list for each bill, with bill.id as a key
        winner_wheels = {bill.id: [] for bill in self.bills}
        for extraction in self.extractions:
            for bill in self.bills:
                # retrieve a winner nums as a list
                winner_nums = check_play_numbers(bill.numbers, bill.play_type, self.extractions[extraction].numbers)
                if (winner_nums and bill.city == 'tutte') or (winner_nums and bill.city == self.extractions[extraction].city):
                    winner_wheels[bill.id].append([bill.play_type, self.extractions[extraction].city, winner_nums])
        return winner_wheels
