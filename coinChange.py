#!/usr/bin/python

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        target = amount
        change = []
        numCoins = len(coins)

        while target > 0:
            i = numCoins - 1 
            while i >= 0:
                print "coin = " + str(coins[i]) + " target = " + str(target)

                if coins[i] > target: 
                    print str(coins[i]) + " coin is too big"
                    i -= 1
                    continue

                if coins[i] == target:
                    print "found final coin"
                    change.append(coins[i])
                    return change

                testTarget = target - coins[i]

                if self.isDivisor(coins, testTarget):
                    print "appending coin " + str(coins[i])
                    change.append(coins[i])
                    target = testTarget
                    break
                else:
                    print "Can't find solution!"
                    return []

                i-=1
        return change

    def isDivisor(self, coins, target):
        for coin in coins:
            if target % coin == 0:
                return True
        return False


soln = Solution()
amount = 12 
coins = [5,7]
print soln.coinChange(coins,amount)
