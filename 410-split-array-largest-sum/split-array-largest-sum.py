class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def cansplit(number):
            parts = 1
            curr = 0

            for num in nums:
                if curr + num > number:
                    parts += 1
                    curr = 0
                curr += num

            return parts <= k
        
        left = max(nums)
        right = sum(nums)

        while left < right:

            mid = (left + right) // 2

            if cansplit(mid):
                right = mid
            else:
                left = mid + 1
            
        return left