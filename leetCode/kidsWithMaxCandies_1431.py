class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = [i + extraCandies >= max(candies) for i in candies]
    
        
        return result
    
a = Solution()    
print(a.kidsWithCandies([2,3,5,1,3], 3))
