class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        demo = nums[0]
        max_sum = demo

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                demo = 0
            demo += nums[i]
            max_sum = max(max_sum, demo)

        return max_sum