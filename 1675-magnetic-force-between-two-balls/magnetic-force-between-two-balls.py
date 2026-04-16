class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def canplace(dist):
            count = 1
            start = position[0]

            for i in range(1, len(position)):
                if position[i] - start >= dist:
                    count += 1
                    start = position[i]
                
                if count == m:
                    return True
            
            return False
        
        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:

            mid = (left + right) // 2

            if canplace(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans