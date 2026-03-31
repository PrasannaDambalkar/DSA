class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1

        n = len(nums)

        while left < n-1:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]

            right += 1

            if right == n:
                left += 1
                right = left + 1