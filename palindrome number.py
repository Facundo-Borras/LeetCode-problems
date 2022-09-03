class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        palindrome = True
        i = 0
        j = len(x) -1
        while palindrome and i < len(x): 
            if x[i] != x[j]:
                palindrome = False
            i += 1
            j -= 1
        return palindrome