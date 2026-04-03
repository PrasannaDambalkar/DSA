class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        mini = float('inf')

        for i in range(len(nums)):
            diff = abs(nums[i]-0)

            mini = min(mini, diff)

        if mini in nums:
            return mini
        else:
            return -mini