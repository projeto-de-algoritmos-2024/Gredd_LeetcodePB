class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas, total_cost = sum(gas), sum(cost)
        if total_gas < total_cost:
            return -1 

