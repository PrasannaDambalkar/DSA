class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        first = None

        for i in range(len(candies)):
            curr = candies[i]
            if first == None or curr > first:
                first = curr

        for i in range(len(candies)):
            if candies[i]+extraCandies >= first:
                candies[i] = True
            else:
                candies[i] = False
        return candies