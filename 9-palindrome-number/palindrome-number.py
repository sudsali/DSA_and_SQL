class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        if x < 0 or (x % 10 == 0 and x!=0):
            return False

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        return reversed_num == x or (reversed_num // 10) == x