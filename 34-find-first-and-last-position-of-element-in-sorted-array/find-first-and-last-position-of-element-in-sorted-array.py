class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        final = [-1,-1]

        while left <= right:

            mid = (left + right)//2
            temp = mid

            if nums[mid] == target:

                while mid >= 0 and nums[mid] == target :

                    final[0] = mid
                    mid -= 1
                
                while temp < len(nums) and nums[temp] == target:

                    final[1] = temp
                    temp += 1
                
                return final
            
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return final