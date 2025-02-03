class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        rev = ['' for i in s]
        front = 0
        back = len(s) - 1
        
        while front <= back:
            if s[front] not in vowels:
                rev[front] = s[front]
                front += 1
            else:
                while s[back] not in vowels and back > front:
                    rev[back] = s[back]
                    back -= 1
                rev[front] = s[back]
                rev[back] = s[front]
                back -= 1
                front += 1


        return ''.join(rev)
    
a = Solution()

print(a.reverseVowels('Pulastya'))
print(a.reverseVowels('aiUouA'))