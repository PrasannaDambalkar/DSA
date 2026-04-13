class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        max_num = arr[-1]
        count = 0

        for i in range(1, max_num + 1):
            if i not in arr:
                count += 1
                if count == k:
                    return i
        
        return max_num + k - count