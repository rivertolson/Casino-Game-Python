import random
import pickle

"""
    This is a casino simulator
"""

# Opens the file with the currency and reads it.
infile = open('casinoCurrency','rb')
currency = pickle.load(infile)
infile.close()

######### Beginging of functions #########

# ----- Counter -----

def counter(money, chips):
    print("Welocme! Chips are $1 each, how many would you like to purchase?")
    buyChips = ''
    while True:
        # This makes sure the player enters a number.
        try:
            buyChips = int(input())
        except ValueError:
            print("Please enter an integer")
            continue

        # This makes sure the player enter a number
        # greater than 0.
        if (buyChips < 1):
            print("Please enter an integer greater than 0")
            continue

        # This makes sure the player cannot spend more
        # money than they have.
        if (money - buyChips < 0):
            print("You cannot spend more than you have")
            continue
        else:
            break

    # Subtracts the correct amount of money
    # and adds the correct amount of chips.
    money = money - buyChips
    chips = chips + buyChips

    moneyFormat = "${:,}".format(money)
    print('')
    print("chips:%s" % chips)
    print("money:%s" % moneyFormat)
    print('')
    print("Thank you and good luck!")
    return (money, chips)

# --- Slots game ---

def slots(money, chips):
    # Game UI Thingy
    while True:
        # moneyFormat is here to configure any money changes that may occur
        moneyFormat = "${:,}".format(money)
        print("Welcome to slots! Would you like to play? (y/n)")

        replay = ('')
        while (replay != 'n' or replay != 'y'):
            replay = str(input())
            if (replay == 'n'):
                break
            elif (replay == 'y'):
                break
            else:
                print("Please enter y or n")
        if (replay == 'n'):
            # Opens the currency file to be written to and replaces
            # the existing dictionary with an updated one.
            # Saves the game when the player leaves the game.
            currency = {'chips': int(chips), 'money': int(money)}
            infile = open('casinoCurrency','wb')
            pickle.dump(currency,infile)
            infile.close()
            break

        print('')
        print("chips: %s" % chips)
        print("money: %s" % moneyFormat)
        print('')

        # Checks if the player has chips to play with.
        # If they are out then ask them if they want to
        # by more.
        if (chips <= 0):
            print("Oh no! it looks like you're all out of chips!")
            print("Would you like to go to the counter and buy more? (y/n)")

            goToCounter = ''
            while True:
                goToCounter = input()
                if (goToCounter == 'y'):
                    counterValues = counter(money,chips)
                    money = counterValues[0]
                    chips = counterValues[1]
                    break
                elif (goToCounter == 'n'):
                    print("Okay, have a great Day!")
                    break
                else:
                    print("Please enter y or n")
            if (goToCounter == 'n'):
                break
            if (goToCounter == 'y'):
                continue

        else:
            print('')

        print("How many chips would you like to spend?")

        # Choose bet amount
        slotBet = 0
        while True:
            try:
                slotBet = int(input())
            except ValueError:
                print("Please enter an integer")
                continue

            # keeps the player from entering 0 or less
            # and no higher than 15
            if (slotBet < 1):
                print("Please enter an integer greater than 0")
                continue
            elif (slotBet > 15):
                print("No bets higher than 15 chips")
                continue

            # Keeps the player from entering more chips
            # than they have.
            if (chips - slotBet < 0):
                print("You cannot bet more than you have")
                continue
            else:
                break

        # slots game
        while True:
            # spending the chips
            chips = chips - slotBet

            # spinning the machine
            slotOne = random.randint(1,7)
            slotTwo = random.randint(1,7)
            slotThree = random.randint(1,7)

            # Displaying the machine
            print("###########")
            print("# %d  %d  %d #" % (slotOne, slotTwo, slotThree))
            print("###########")

            # Jackpot
            if (slotOne == 7 and slotTwo == 7 and slotThree == 7):
                winnings = slotBet + 500
                chips = chips + winnings
                print("Jackpot!!!")
                print("You won %d chips!" % winnings)
                winnings = 0

            # All matched
            elif (slotOne == slotTwo and slotOne == slotThree):
                winnings = slotBet * 5
                chips = chips + winnings
                print("You matched them all!!")
                print("You won %d chips!" % winnings)
                winnings = 0

            # Two matched
            elif (slotOne == slotTwo or slotTwo == slotThree or slotOne == slotThree):
                winnings = slotBet * 3
                chips = chips + winnings
                print("You matched Two numbers!")
                print("You won %d chips!" % winnings)
                winnings = 0

            else:
                print("You didn't match any")

            print('')
            print("chips: %d" % chips)
            print("money: %s" % moneyFormat)
            print('')

            # if statement triggered if player has no more chips
            if (chips <= 0):
                print("Oh no! It looks like you have ran out of chips!")
                print("Would you like to go to the counter and buy more chips? (y/n)")

                goToCounter = ''
                while True:
                    goToCounter = input()
                    if (goToCounter == 'y'):
                        counterValues = counter(money,chips)
                        money = counterValues[0]
                        chips = counterValues[1]

                        break
                    elif (goToCounter == 'n'):
                        print("Okay, have a great Day!")
                        break
                    else:
                        print("Please enter y or n")
                if (goToCounter == 'n'):
                    break
                if (goToCounter == 'y'):
                    break
                print('')
                break

            # Asks if the player wants to spin again with the same
            # amount of chips.
            if (chips - slotBet >= 0):
                print('')
            else:
                print("It looks like you cannot bet again!")
                break

            print('Would you like to play again? (y/n)')
            replay = ''
            while True:
                replay = str(input())
                if (replay == 'n'):
                    break
                elif (replay == 'y'):
                    break
                else:
                    print("Please enter y or n")
            if (replay == 'n'):
                # Opens the currency file to be written to and replaces
                # the existing dictionary with an updated one.
                currency = {'chips': int(chips), 'money': int(money)}
                infile = open('casinoCurrency','wb')
                pickle.dump(currency,infile)
                infile.close()
                break
    return (money, chips)

""" 
----- Black Jack -----
The objective of black jack is to get a count as close to 21 as possible
without going over 21.

== SETTING UP ==
* It is up to each player if ace is worth 1 or 11.
* Face cards are worth 10.
* Any other card is worth its face value.
* Minimum bet of 2 and max of 500.

== Gameplay ==
* The player gets two faceup cards.
* The dealer(game) gets one face up card and one facedown card.
* If the players cards are equal to 21 off of the draw that player has a
  blackjack. If the player has a blackjack and the dealer does not then the
  player automatically wins 1.5 times their bet.
* If the player and the dealer have a blackjack then the player takes their
  bet back.
"""
######### End of functions #########

# Saves the currencies from the dictionary in the casinoCurrency file
chips = currency["chips"]
money = currency["money"]
# Formating money
moneyFormat = "${:,}".format(money)

# ===== Start of the Casino game =====
print("Welcome to the casino! v0.0.1")

playerChoice = ('')
while True:
    # Reformats money
    moneyFormat = "${:,}".format(money)
    print('')
    print("chips: %s" % chips)
    print("money: %s" % moneyFormat)
    print('')
    print("What would you like to do?")
    print('')
    print('(1) Go to the counter')
    print('(2) Play slots')
    print('(0) Exit')
    try:
        playerChoice = int(input())
    except ValueError:
        print("Please put a number")
        continue

    if(playerChoice == 1 or playerChoice == 2):
        if(playerChoice == 1):
            counterValues = counter(money,chips)
            money = counterValues[0]
            chips = counterValues[1]
        else:
            slotsCurrency = slots(money, chips)
            money = slotsCurrency[0]
            chips = slotsCurrency[1]
    elif(playerChoice == 0):
        print("Have a good day!")
        # Saves the players chips before they quit the game.
        currency = {'chips': int(chips), 'money': int(money)}
        infile = open('casinoCurrency','wb')
        pickle.dump(currency,infile)
        infile.close()
        quit()
    else:
        print("Please enter one of the options given")
