class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        status = False
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]



        # len_nums = len(nums)
        # dict_nums = {i:nums[i] for i in range(len_nums)}
        # index_on_sorted_value = list(dict(sorted(dict_nums.items(), key=lambda item: item[1])))


        # for i in range(2, len_nums):
        #     if index_on_sorted_value[i] > index_on_sorted_value[i-1] > index_on_sorted_value[i-2]:
        #         status = True
        #         break
        
        # return index_on_sorted_value


a = Solution()

print(a.increasingTriplet([2,1,5,0,4,6]))
            