#!/usr/bin/python
def solve(a0, a1, a2, b0, b1, b2):
    aScore = 0
    bScore = 0
    aScore,bScore = score(a0,b0,aScore,bScore)
    aScore,bScore = score(a1,b1,aScore,bScore)
    aScore,bScore = score(a2,b2,aScore,bScore)
    print str(aScore) + " " + str(bScore)

def score(a,b,aScore,bScore):
    if a > b:
        aScore +=1
    elif b > a:
        bScore +=1
    return (a,b)

solve(1,1,2,3,4,5)
