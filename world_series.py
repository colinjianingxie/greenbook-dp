
'''
From 7 games, need to win 4, You have $100. How should you optimize your bets such that at the end, you will either win 100 or lose 100.
'''



def get_wins_needed(n=7):
    return n // 2 + 1

def generate_tree(n=7):
    arr_len = get_wins_needed(n) + 1
    res = []

    for i in range(arr_len):
        res.append([0] * arr_len)

    return res

def print_soln(arr):
    print("Rows are opponents (lose)")
    print("Columns are team (win)")
    for i in range(len(arr)):
        s = ["%5.2f" % k if k < 0 else "+%5.2f" % k for k in arr[i]]
        temp = '   '.join(s)
        print(f'{temp}')

def build_soln(n, capital=100):
    payoff_tree = generate_tree(n)
    delta_tree = generate_tree(n)

    wins_needed = get_wins_needed(n)

    for i in range(wins_needed, -1, -1):
        for j in range(wins_needed, -1, -1):
            if i == j:
                continue
            if i == wins_needed:
                # For initial cases
                payoff_tree[i][j] = -capital
            elif j == wins_needed:
                payoff_tree[i][j] = capital
            else:
                payoffs = (payoff_tree[i+1][j] + payoff_tree[i][j+1]) / 2
                payoff_tree[i][j] = payoffs

    for i in range(wins_needed-1, -1, -1):
        for j in range(wins_needed-1, -1, -1):
            delta_tree[i][j] = (payoff_tree[i][j+1] - payoff_tree[i+1][j]) / 2
    return (payoff_tree, delta_tree)

def main():
    number_games = 7
    capital = 100
    payoff_res, delta_res = build_soln(number_games, capital=capital)
    print("\n\n\nCurrent payoffs at each stage")
    print_soln(payoff_res)

    print("\n\n\nBets needed to be made: ")
    print_soln(delta_res)

main()
