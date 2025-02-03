class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len = min(len(str1), len(str2))
        large_repeating_str = ''

        for i in range(min_len):
            if str1[i] == str2[i]:
                large_repeating_str = large_repeating_str
                str1.split()

        # if len_str1 % len_str2 != 0 and len_str2 % len_str1 != 0 and len_str1 % 2 != 0 and len_str2 % 2 != 0:
        #     return '' 
        # else:
