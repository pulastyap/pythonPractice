class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        merged_str = ''
        for i in range(min_length):
            merged_str += word1[i]
            merged_str += word2[i]
        
        merged_str += word1[min_length: len(word1)]
        merged_str += word2[min_length: len(word2)]

        return merged_str

a = Solution()

print(a.mergeAlternately('Pandey', 'Pulastya'))