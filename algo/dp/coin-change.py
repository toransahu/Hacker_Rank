#!/bin/python3

import sys
"""
URL: https://www.hackerrank.com/challenges/coin-change
"""


def getWays(amount, all_coins):
    # Complete this function
    global count
    if len(all_coins) == 1:
        if amount % all_coins[0] == 0:
            count += 1
            return 1
        else:
            return 0
    else:
        coins = sorted(all_coins, reverse = True)
        for i in range((amount // coins[0]) + 1):
             getWays(amount - (i * coins[0]), coins[1:])
    return count


# amount, no_of_deno = input().strip().split(' ')
# amount, no_of_deno = [int(amount), int(no_of_deno)]
# all_coins = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'amount' units using coins having the values given by 'all_coins'
count = 0
ways = getWays(4, [1, 2, 3])
print(ways)
#print(count)
