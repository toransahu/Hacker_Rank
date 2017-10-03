import sys
"""
URL: https://www.hackerrank.com/challenges/coin-change
"""

amount = 4
no_of_deno = 4
all_coins = [8, 3, 1, 2]
# create list with 5 list and (m+1) element in each
memo = [[0 for i in range(no_of_deno + 1)] for j in range(no_of_deno + 1)]
coins = [i for i in all_coins if i <= amount]
way = 0

for i in coins:
    for j in ccoins:
        if i != j and (memo[i][j] == 1 or memo[j][i] == 1):
            way += 1
        elif i != j and i + j == n:
            memo[i][j] = 1
            memo[j][i] = 1
            way += 1

for i in range(amount // min(coins)):
    for j in coins:
        if j * i == amount:
            way += 1
return way
