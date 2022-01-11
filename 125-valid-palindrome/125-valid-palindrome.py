class Solution:
    def isPalindrome(self, s):
        s = str(s)
        s = self._clean_string(s)
        
        left_pointer = 0
        right_pointer = len(s) - 1
        
        while not left_pointer >= right_pointer:
            if not s[left_pointer] == s[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        
        return True
        
        
    def _clean_string(self, s):
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        return s