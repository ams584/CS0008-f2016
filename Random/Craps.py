import random
a = 0
starting_cash = 1000
print("Rules: If the sum of the dice is 7, you lose.")
print("Balance: ", starting_cash)
bet = int(input("How much do you want to bet? "))
z = 0
while z == 0:
    if bet > starting_cash:
        print("You don't have that much money.")
        bet = int(input("How much do you want to bet? "))
    else:
        z = 1
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
print("First die: ", d1, "Second die: ", d2)
if d1 + d2 == 7:
    print("You lose.")
    balance = starting_cash - bet
    print("Your balance is: ", balance)
else:
    print("You win.")
    balance = starting_cash + bet
    print("Your balance is: ", balance)
balance = balance
while a == 0:
    if balance != 0:
        play_again = str(input("Would you like to play again? Enter 'y' or 'n'"))
        if play_again == "y":
            bet = int(input("How much do you want to bet? "))
            z = 0
            while z == 0:
                if bet > balance:
                    print("You don't have that much money.")
                    bet = int(input("How much do you want to bet? "))
                else:
                    z = 1
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            print("First die: ", d1, "Second die: ", d2)
            if d1 + d2 == 7:
                print("You lose.")
                balance = balance - bet
                print("Your balance is: ", balance)
            else:
                print("You win.")
                balance = balance + bet
                print("Your balance is: ", balance)
            balance = balance
        else:
            a = 1
    else:
        print("You are out of cash.")

