class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        if len(dist) - 1 >= hour:
            return -1
        
        left = 1
        right = 10**7

        def canspeed(speed):
            time = 0

            for i in range(len(dist) - 1):
                time += (dist[i] + speed - 1) // speed

            time += dist[-1] / speed
        
            return time <= hour

        while left < right:
            mid = (left + right) // 2

            if canspeed(mid):
                right = mid
            else:
                left = mid + 1
        
        return left