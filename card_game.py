'''
Each red card drawn is +$1
Each black card drawn is $-1

What's th optimal rule in maximizing expected payoff, how much are you willing to play?
'''

def create_deck(black, red):
    arr = []
    for i in range(0, black+1):
        arr.append([i] + [0]*(red))

    return arr

def print_arr(arr):
    for row in arr:
        temp = ' '.join(["%3.2f" % i for i in row])
        print(f"{temp}")

def soln(black, red):
    '''
    let B = current black left in deck, R = current red left in deck.

    payoff is B-R at state(B, R)

    if we continue, the max_payoff would be:

        max(B-R, b/(b+r) * [b-1][r] + r/(b+r) * [b][r+1])
    '''
    arr = create_deck(black, red)
    for b in range(1, black+1):
        for r in range(1, red+1):
            b_p = b/(b+r)
            r_p = r/(b+r)

            arr[b][r] = max(b-r, b_p * arr[b-1][r] + r_p * arr[b][r-1])

    print_arr(arr)
    print("------")
    print("Should pay: ", arr[-1][-1])

def main():
    # Number left in deck...
    red = 26
    black = 26

    soln(black, red)


main()
