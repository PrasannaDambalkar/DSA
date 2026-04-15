class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix = {0 : -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem in prefix:
                if (i - prefix[rem]) >= 2:
                    return True
            else:
                prefix[rem] = i
        return False