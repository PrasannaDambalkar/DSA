class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        temp = 0
        start = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            temp += gas[i] - cost[i]

            if temp < 0:
                start = i + 1
                temp = 0

        return start