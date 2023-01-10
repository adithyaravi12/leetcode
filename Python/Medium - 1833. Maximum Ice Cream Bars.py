class Solution(object):
    def maxIceCream(self, costs, coins):
        buy_count = 0
        costs.sort()
        print(costs)
        for x in range(len(costs)):
            print x
            if costs[x] <= coins:
                coins = coins - costs[x]
                buy_count += 1
            else:
                break
        return buy_count