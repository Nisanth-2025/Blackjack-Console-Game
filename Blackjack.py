import random
from random import choice

# Assign Part
deck1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J']
main_deck = 4 * deck1


# Assign cards for Player
def player_assign():
    random.shuffle(main_deck)
    player_hand = [random.choice(main_deck), random.choice(main_deck)]
    return player_hand


# Assign cards for Dealer
def dealer_assign():
    random.shuffle(main_deck)
    dealer_hand = [random.choice(main_deck), random.choice(main_deck)]
    return dealer_hand


# Calculates total for player cards
def calc_total(temp_total):
    total = 0
    for val in temp_total:
        if (str(val).isdigit()):
            total += int(val)
        else:
            if (val == 'A'):
                if (total <= 10):
                    total += 11
                else:
                    total += 1
            else:
                total += 10
    return total


# Process when players hits
def player_hit(result1):
    random.shuffle(main_deck)
    result1.append(random.choice(main_deck))
    return result1


def dealer_hit(result2):
    random.shuffle(main_deck)
    result2.append(random.choice(main_deck))
    return result2


# Main Block

while True:
    result1 = player_assign()
    result2 = dealer_assign()
    print(f'\t\t\t\tGAME BEGINS')
    print()
    print(f'Player Hand:{result1}')
    print(f'Player Total:{calc_total(result1)}')
    print(f'Dealer Hand:{result2[0], 'Card Faced Down'}')
    print(f'Your Turn...')
    while True:
        chose = input(f'1.Hit\n2.Stand\n')
        if chose == '1':
            result1 = player_hit(result1)
            if calc_total(result1) < 21:
                print(f'Player Hand:{result1}')
                print(f'Player Total:{calc_total(result1)}')
                print(f'Dealer Hand:{result2[0], 'Card Faced Down'}')
            elif calc_total(result1) == 21:

                if calc_total(result1) == calc_total(
                        result2):  # make change as per tie rules .no tie natue of cards ace na dking
                    print(f'Player Hand:{result1}')
                    print(f'Player Total:{calc_total(result1)}')
                    print(f'Dealer Hand:{result2[0], result2[1]}')
                    print(f'Dealer Total:{calc_total(result2)}')
                    print(f'Game Tie,No One Wins')
                    break

                else:
                    print(f'Player Hand:{result1}')
                    print(f'Player Total:{calc_total(result1)}')  # make change ''''
                    print(f'Dealer Hand:{result2[0], result2[1]}')
                    print(f'Dealer Total:{calc_total(result2)}')
                    print(f'You Win ,Dealer Busted')
                    break
            else:
                print(f'Player Hand:{result1}')
                print(f'Player Total:{calc_total(result1)}')
                print(f'Dealer Hand:{result2[0], result2[1]}')
                print(f'Dealer Total:{calc_total(result2)}')
                print(f'You Busted.Dealer wins')
                print(f'You Lose')
                break

        elif (chose == '2'):
            print(f'Dealer\'s Turn..')
            print()

            while True:
                if calc_total(result2) <= 16:
                    print(f'Dealer Hit\'s')
                    result2 = dealer_hit(result2)
                    if calc_total(result2) <= 16:
                        print(f'Player Hand:{result1}')
                        print(f'Player Total:{calc_total(result1)}')
                        print(f'Dealer Hand:{result2}')
                        print(f'Dealer Total:{calc_total(result2)}')
                    elif calc_total(result2) > 16:
                        print(f'Player Hand:{result1}')
                        print(f'Player Total:{calc_total(result1)}')
                        print(f'Dealer Hand:{result2}')
                        print(f'Dealer Total:{calc_total(result2)}')
                        if calc_total(result2) > calc_total(result1) and calc_total(result2) <= 21:
                            print(f'Dealer Wins,Player Busted.')
                            print(f'You Lose')
                            break
                        elif calc_total(result2) == calc_total(result1):  # change tie aas per condition
                            print(f'Player Hand:{result1}')
                            print(f'Player Total:{calc_total(result1)}')
                            print(f'Dealer Hand:{result2[0], result2[1]}')
                            print(f'Dealer Total:{calc_total(result2)}')
                            print(f'Game Tie,No One Wins')
                            break
                        else:
                            print(f'Player Win\'s,Dealer Busted')
                            break
                    else:
                        pass

                elif calc_total(result2) > 16:
                    print(f'Dealer Stay\'s')
                    print(f'Player Hand:{result1}')
                    print(f'Player Total:{calc_total(result1)}')
                    print(f'Dealer Hand:{result2}')
                    print(f'Dealer Total:{calc_total(result2)}')
                    if calc_total(result2) == calc_total(result1) != 21:
                        print(f'Game Tie,No One Wins')
                        break
                    elif calc_total(result2) > calc_total(result1) and calc_total(result2) <= 21:
                        print(f'Dealer Wins,Player Busted.')
                        print(f'You Lose')
                        break
                    elif calc_total(result2) == calc_total(result1) == 21:  # check for tie
                        print(f'Game Tie,No One Wins')
                        break
                    else:
                        print(f'Player Win\'s,Dealer Busted')
                        break
            break


        else:
            print(f'Please Enter a valid Input.Try Again')

    y_n = input("Do You want to continue:[Y/N]:")
    if y_n.lower() == 'n':
        break
    else:
        print()