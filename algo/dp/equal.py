"""
DP Problem
URL: https://www.hackerrank.com/challenges/equal
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

def min_ops(interns):
    solved = -1
    no_ops = 0
    while(solved == -1):
        interns = sorted(interns, reverse=True)
        min_choc = min(interns)
        max_choc = max(interns)
        if min_choc == max_choc:
            solved = 1
                
        if max_choc - min_choc >= 5:
            interns[0] = interns[0] - 5
            no_ops+=1
        elif max_choc - min_choc >= 2:
            interns[0] = interns[0] - 2
            no_ops+=1
        elif max_choc - min_choc >= 1:
            interns[0] = interns[0] - 1
            no_ops+=1
    return no_ops


t = int(input().strip())
for _ in range(t):
    no_intern = int(input().strip())
    interns = sorted(map (int,input().strip().split(' ')))
    solved = False
    print(min_ops(interns))
