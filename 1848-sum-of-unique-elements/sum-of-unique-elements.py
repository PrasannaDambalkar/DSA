class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] = 0

        final = [a for a, b in freq.items() if b == 1]

        return sum(final)