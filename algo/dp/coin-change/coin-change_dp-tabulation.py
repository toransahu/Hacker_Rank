#!/bin/python3
"""
Problem: Coin change.

Approach: DP-Tabulation
URL: https://www.hackerrank.com/challenges/coin-change
"""


# import sys


def getWays(amount, coins):
    """Find number of ways."""
    coins = sorted(coins)
    # create a table of lenght amount + 1
    # fill 0th with 1 i.e. way of making 0 rupay = 1
    # fill rest with 0

    ways = [1] + [0] * amount

    # find ways of each amount till given amount
    for coin in coins:
        # start from current amount till amount given
        for i in range(coin, amount+1):
            # ways of current amount = ways of current amount till now + ways of (current amount - current coin)
            ways[i] += ways[i - coin]
    return ways[amount]


# amount, no_of_deno = input().strip().split(' ')
# amount, no_of_deno = [int(amount), int(no_of_deno)]
# all_coins = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'amount' units
# using coins having the values given by 'all_coins'
ways = getWays(4, [1, 2, 3])
print(ways)
