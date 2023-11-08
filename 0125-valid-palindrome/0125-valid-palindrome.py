class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.split('[^a-z0-9]', s.lower()))
        return s == s[::-1]