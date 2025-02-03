class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 2

        available_space = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0: return 1 >= n
            else: return 0 == n
        elif flowerbed[0] == flowerbed[1] == 0: available_space += 1; flowerbed[0] = 1
        max_range = len(flowerbed) - 1
        
        while i < max_range:
            if flowerbed[i] == 1: i += 2
            elif flowerbed[i-1] == 1: i += 1
            elif flowerbed[i+1] == 1: i += 2
            else: available_space += 1; flowerbed[i] = 1; i += 2

        if flowerbed[max_range] == flowerbed[max_range - 1] == 0: available_space += 1

        return n <= available_space

a = Solution()

print(a.canPlaceFlowers([0], 0))
