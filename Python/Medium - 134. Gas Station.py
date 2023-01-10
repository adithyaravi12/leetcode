class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = ind = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            total = total + (gas[i] - cost[i])
            if total < 0:
                ind = i + 1
                total = 0
        return ind
        
        