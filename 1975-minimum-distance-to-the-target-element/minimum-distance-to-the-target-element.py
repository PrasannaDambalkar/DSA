class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        core = float('inf')

        for i in range(len(nums)):
            if nums[i] == target:
                core = min(core, abs(i-start))

        return core