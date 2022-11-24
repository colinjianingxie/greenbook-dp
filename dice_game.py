import random

'''
Allowed to keep rolling dice until you hit stopping_value.

You get the face value as $.

What's the maximum amount you pay to play game assuming risk neutral?

'''

class Dice:
    def __init__(self, min_val, max_val, stopping_val):
        self.dice_min = min_val
        self.dice_max = max_val
        self.stopping_val = stopping_val

    def random_value(self):
        return random.randint(self.dice_min, self.dice_max)

    def generate_payoff(self):
        curr = self.random_value()
        if curr == self.stopping_val:
            return 0, 1

        total = curr
        counter = 1
        while curr != self.stopping_val:
            total += curr
            curr = self.random_value()
            counter += 1

        return total, counter

    def rolls(self):
        return [i for i in range(self.dice_min, self.dice_max+1)]

    def rolls_without_stopping(self):
        return [i for i in range(self.dice_min, self.dice_max+1) if i != self.stopping_val]

    def max_rolls_without_stopping(self):
        return max(self.rolls_without_stopping())

    def expected_dice_roll(self):
        return (sum(self.rolls()) - self.stopping_val) / len(self.rolls())

    def keep_rolling_until(self):
        '''
            keep rolling if: 5n/6 + expected_dice_roll(6) > n
        '''
        return int((self.dice_max - self.dice_min + 1) * self.expected_dice_roll())

    def generate_base_payoffs(self):
        return [0] * (self.keep_rolling_until() + self.max_rolls_without_stopping())

def soln(dice):
    '''
    assume we have n dollars accumulated.

    The decision to roll or not depends on profit vs expected loss.

    if we decide to do extra roll:

    payoff becomes: 5/6 * n + expected_dice_roll(6)

    '''
    arr = dice.generate_base_payoffs()

    for i in range(len(arr)-1, -1, -1):
        if i >= dice.keep_rolling_until():
            arr[i] = i
        else:
            arr[i] = 1/6 * (sum(arr[i+j] for j in dice.rolls_without_stopping()))

    print("----- payoffs -----")
    for i in range(len(arr)):
        print(f"{i}: {arr[i]}")


    return arr[0]

def simulate(dice, num_trials = 1000):
    total_payoffs = 0
    total_rolls = 0
    for i in range(num_trials):
        temp_payoff, num_rolls = dice.generate_payoff()
        total_payoffs += temp_payoff
        total_rolls += num_rolls

    average_payoff = total_payoffs / num_trials
    average_rolls = total_rolls/num_trials
    print(f"{average_payoff} average payoff with {average_rolls} rolls")
    print(average_payoff/average_rolls)

def main():
    stopping_value = 6
    dice = Dice(min_val=1, max_val=6, stopping_val=stopping_value)
    print(soln(dice))
    simulate(dice, 100000)

main()
