import sys

"""
URL: https://www.hackerrank.com/challenges/coin-change
"""

m = 4
c = [8,3,1,2]
n = 4
# create list with 5 list and (m+1) element in each
memo = [[0 for i in range(m+1)] for j in range(5)]
cn = [i for i in c if  i<=n ]
way = 0

for i in cn:
    for j in cn:
        if i!=j and (memo[i][j]==1 or memo[j][i]==1):
            way+=1
        elif i!=j and i+j == n:
            memo[i][j]=1
            memo[j][i]=1
            way+=1
            
for i in range(n//min(cn)):
    for j in cn:
        if j*i==n:
            way+=1
return  way
