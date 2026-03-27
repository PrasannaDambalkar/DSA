class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        gain.insert(0, 0)
        final = 0
        for i in range(1, len(gain)):
            gain[i] = gain[i-1]+gain[i]

            final = max(gain[i], final)
        
        return final