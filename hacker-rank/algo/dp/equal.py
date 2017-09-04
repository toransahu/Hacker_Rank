"""
DP Problem
URL: https://www.hackerrank.com/challenges/equal
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def min_ops(interns):
    min_choc = min(intern)
    max_choc = max(intern)
    no_ops = 0
    solved = -1
    if min_choc == max_choc:
        return [no_ops,solved]
    if max_choc - min_choc >= 5:



    return [no_ops,solved]


t = int(input().strip())
for _ in range(t):
    no_intern = int(input().strip())
    interns = sorted(map (int,input().strip().split(' ')))
    solved = False
    no_ops =
