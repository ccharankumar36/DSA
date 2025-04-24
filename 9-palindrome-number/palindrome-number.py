class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while x >= 10 * div:
            div *= 10
        while x:
            left = x % 10
            right = x // div
            if left != right:
                return False
            x = (x % div) // 10
            div = div // 100
        return True
        
        