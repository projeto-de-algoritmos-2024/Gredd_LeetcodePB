class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        N = len(gas)
        gas = gas + gas
        cost = cost + cost
        current = 0
        start = 0