#!/bin/python3

import sys
"""
URL: https://www.hackerrank.com/challenges/coin-change
"""

import sys


def getWays(amount, all_coins):
    # Complete this function
    coins = [i for i in all_coins if i <= amount]
    no_of_deno = len(coins)
    memo = [[0 for i in range(no_of_deno + 1)] for j in range(no_of_deno + 1)]

    way = 0

    for i in coins:
        for j in coins:
            if i != j and (memo[i][j] == 1 or memo[j][i] == 1):
                way += 1
            elif i != j and i + j == amount:
                memo[i][j] = 1
                memo[j][i] = 1
                way += 1

    for i in range(amount // min(coins)):
        for j in coins:
            if j * i == amount:
                way += 1
    return way


amount, no_of_deno = input().strip().split(' ')
amount, no_of_deno = [int(amount), int(no_of_deno)]
all_coins = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'amount' units using coins having the values given by 'all_coins'
ways = getWays(4, '1 2 3')
print(ways)
