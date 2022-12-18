import random


def roll_dice_until(n, total):
    randomNumber = random.randint(1, 6)
    if randomNumber in n:
        return total
    else:
        return roll_dice_until(n, total + randomNumber)


def main():

    number_simulations = 10000
    stopping = [2]
    total = 0
    for i in range(number_simulations):
        total += (roll_dice_until(stopping, 0))


    print(total / number_simulations)

main()
