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
    ways = [1] + [0] * amount
    for coin in coins:
        for i in range(coin, amount+1):
            ways[i] += ways[i - coin]
    return count


# amount, no_of_deno = input().strip().split(' ')
# amount, no_of_deno = [int(amount), int(no_of_deno)]
# all_coins = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'amount' units
# using coins having the values given by 'all_coins'
ways = getWays(4, [1, 2, 3])
print(ways)
