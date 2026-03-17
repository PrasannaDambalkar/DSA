class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        first = None
        second = None

        for i in range(len(nums)):
            curr = nums[i]
            if first == None or curr >= first:
                second = first
                first = curr
            elif second == None or curr >= second:
                second = curr

        return (first-1)*(second-1)