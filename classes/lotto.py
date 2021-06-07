def check_play_numbers(bill_numbers, bill_play_type, money_bet, extraction_numbers):
    count_win_numbers = 0
    winner_nums = []
    for bill_n in bill_numbers:
        for ext_n in extraction_numbers:
            if bill_n == ext_n:
                winner_nums.append(bill_n)
                count_win_numbers += 1
    for k in Lotto.TYPE_PLAY:
        if k == bill_play_type and Lotto.TYPE_PLAY[k] == count_win_numbers:
            money_win = money_bet * Lotto.GROSS_WINNERS_DATA[len(bill_numbers)][count_win_numbers-1]
            return winner_nums, money_win
    return False, 0


class Lotto:
    TYPE_PLAY = {'estratto': 1, 'ambo': 2, 'terno': 3, 'quaterna': 4, 'cinquina': 5}
    NUMBERS = [n for n in range(1, 11)]
    NAME_CITIES = ['bari', 'cagliari', 'firenze', 'genova', 'roma', 'palermo', 'torino', 'venezia', 'milano', 'napoli']
    GROSS_WINNERS_DATA = {1: [11.23], 2: [5.61, 250], 3: [3.74, 83.33, 4500], 4: [2.80, 41.66, 1125, 120.000],
                    5: [2.24, 25, 450, 24.000, 6_000_000],
                    6: [1.87, 16.66, 225, 8.000, 1_000_000], 7: [1.60, 11.90, 128.57, 3428.57, 285_714.28],
                    8: [1.40, 8.92, 80.35, 1_714.28, 107_142.85], 9: [1.24,	6.94, 53.57, 952.38, 47_619.04],
                    10: [1.12, 5.55, 37.50, 571.42, 23_809.52]}

    def __init__(self, bills, extractions):
        self.bills = bills
        self.extractions = extractions

    def winner_wheels(self):
        # create a dict of list for each bill, with bill.id as a key
        winner_wheels = {bill.id: [] for bill in self.bills}
        for extraction in self.extractions:
            for bill in self.bills:
                # retrieve a winner nums and money as a list and numeric value
                winner_nums, money_win = check_play_numbers(bill.numbers, bill.play_type, bill.money_bet, self.extractions[extraction].numbers)
                if winner_nums and bill.city == self.extractions[extraction].city:
                    winner_wheels[bill.id].append([bill.play_type, self.extractions[extraction].city, winner_nums, money_win])
                elif winner_nums and bill.city == 'tutte':
                    winner_wheels[bill.id].append([bill.play_type, 'Tutte, first: ' + self.extractions[extraction].city, winner_nums, money_win])
                    return winner_wheels
        return winner_wheels
