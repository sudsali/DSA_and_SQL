class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l <= r :
            if s[l].isalpha() or s[l].isdigit():
                if s[r].isalpha() or s[r].isdigit():
                    if s[l] != s[r]:
                        return False
                    else:
                        l+=1
                        r-=1
                else:
                    r-=1
            else:
                l+=1
        return True