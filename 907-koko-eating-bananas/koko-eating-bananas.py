class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        def caneat(hour):
            hours = 0

            for pile in piles:
                hours += (pile + hour - 1) // hour

                if hours > h:
                    return False
            return True


        while left < right:

            mid = (left + right) // 2

            if caneat(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
