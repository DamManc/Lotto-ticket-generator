from classes.bill import Bill

TYPE_PLAY = ['estratto', 'ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
NUMBERS = [n for n in range(1, 11)]
NAME_CITIES = ['bari', 'cagliari', 'firenze', 'genova', 'roma', 'palermo', 'torino', 'venezia', 'milano', 'napoli', 'tutte']


def check_input_answ(question, poss_response):
    print(question)
    usr_in = input()
    while usr_in:
        if poss_response is TYPE_PLAY or poss_response is NAME_CITIES:
            usr_in = usr_in.lower()
        else:
            usr_in = int(usr_in)
        if usr_in in poss_response:
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
                for _ in range(1, 4):
                    if _ == 1:
                        question = f'Which type of play for the bill number {i} (estratto, ambo, terno, quaterna, ' \
                                   f'cinquina)? '
                        poss_response = TYPE_PLAY
                    elif _ == 2:
                        question = f'How many number (1 to 10) for this play?'
                        poss_response = NUMBERS
                    else:
                        question = f'Which city (aka ruota)? (Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, ' \
                                   f'Roma, Torino, Venezia or Tutte )? '
                        poss_response = NAME_CITIES
                    # insert into the answer's list the return value of check_input_answ
                    answers.append(check_input_answ(question, poss_response))
                # create a Bill Object only there are not False value in the answer's list (e.g blank value)
                if False not in answers:
                    bill = Bill(answers[0], answers[1], answers[2])
                    bills.append(bill)
                # if the User decide to leave blank some question, don't create Bill and ask for what he decide to do
                else:
                    print('You haven\'t answer all question, you want to quit and Cancel all bills that you have? Y/n')
                    cancel_input = input()
                    if not cancel_input or cancel_input.lower() == 'y':
                        quit()
                    else:
                        # the possibility to print out your bills up to now
                        print('You want to print out your bills that you have up to now? Y/n')
                        print_bills = input()
                        if not print_bills or print_bills.lower() == 'y':
                            for bill in bills:
                                print(bill)
                        # quit after
                        quit()
            # print out all Bills Objects
            for bill in bills:
                print(bill)
        except ValueError:
            print('Your value entered is not valid, if you you want to quit leave blank')
            main()
    else:
        quit()


if __name__ == '__main__':
    main()
