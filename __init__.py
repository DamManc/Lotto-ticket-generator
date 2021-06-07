from classes.bill import Bill
from classes.extraction import Extraction
from classes.lotto import Lotto


def check_input_answ(question, poss_response):
    print(question)
    usr_in = input()
    while usr_in:
        if poss_response is Lotto.NUMBERS or poss_response == 'all numbers':
            try:
                usr_in = int(usr_in)
            except ValueError:
                check_input_answ(question, poss_response)
        else:
            usr_in = usr_in.lower()
        if poss_response == 'all numbers' or usr_in in poss_response:
            return usr_in
        else:
            print('This value entered is not valid, if you you want to quit leave blank')
            print(question)
            usr_in = input()
    return False


def main():
    num_bills = input('How many bills do you want to generate? (min: 1, max:5, exit:0)\n')
    if num_bills:
        try:
            num_bills = int(num_bills)
            if num_bills < 0 or num_bills > 5:
                raise ValueError
            # create a list of Objects Bill
            bills = []
            # repeat for the number of bills to create
            for i in range(1, num_bills + 1):
                # create a list of possible answers
                answers = []
                for _ in range(1, 5):
                    if _ == 1:
                        question = f'Which type of play for the bill number {i} (estratto, ambo, terno, quaterna, ' \
                                   f'cinquina)? '
                        poss_response = Lotto.TYPE_PLAY
                    elif _ == 2:
                        question = f'How many number (1 to 10) for this play?'
                        poss_response = Lotto.NUMBERS
                    elif _ == 3:
                        question = f'Which city (aka ruota)? (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, ' \
                                   f'Roma, Torino, Venezia or Tutte )? '
                        poss_response = Lotto.NAME_CITIES + ['tutte']
                    else:
                        question = f'How much money?'
                        poss_response = 'all numbers'
                    # insert into the answer's list the return value of check_input_answ
                    answers.append(check_input_answ(question, poss_response))
                # create a Bill Object only there are not False value in the answer's list (e.g blank value)
                if False not in answers:
                    bill = Bill(answers[0], answers[1], answers[2], answers[3])
                    bills.append(bill)
                # if the User decide to leave blank some question, don't create Bill and ask for what he decide to do
                else:
                    print('You haven\'t answer all questions, you want to quit and Cancel all bills that you have? Y/n')
                    cancel_input = input()
                    if not cancel_input or cancel_input.lower() == 'y':
                        quit()
                    else:
                        # the possibility to print out your Bills up to now
                        print('You want to print out your bills that you have up to now and check if you have win? Y/n')
                        print_bills = input()
                        if not print_bills or print_bills.lower() == 'y':
                            break
                        else:
                            quit()

            # print out all your Bills Objects
            print(f'\033[96mYour bill/s is/are: \n')
            for bill in bills:
                print(bill)

            # init a dict for the Extractions Objects
            extractions = {}
            print(f'\033[0mThe Extractions are: \n')

            # create the Extraction Objects and key with name of a city
            for i in range(len(Lotto.NAME_CITIES)):
                ext = Extraction(Lotto.NAME_CITIES[i])
                extractions[Lotto.NAME_CITIES[i]] = ext
                print(ext)

            # create a Lotto Object and retrieve the winner wheels
            winner_wheels = Lotto(bills, extractions).winner_wheels()
            for k_winner in winner_wheels:
                if len(winner_wheels[k_winner]) > 0:
                    print(f'\033[92mYOU HAVE WIN! with The Bill number {k_winner}:\n')
                    for win in winner_wheels[k_winner]:
                        print(f'\033[92mPlay type: {win[0]}\t City/Wheel: {win[1]}\t Winner Number/s {win[2]}\t Gross Money '
                              f'Wins {round(win[3], 2)}\t Net Money Wins {round(win[3] - win[3]* 0.08, 2)} \n')
                else:
                    print(f'\033[93mSorry, you have lose with the bill number {k_winner}\n')

        except ValueError:
            print('Your value entered is not valid, if you you want to quit leave blank')
            main()
    else:
        quit()


if __name__ == '__main__':
    main()
