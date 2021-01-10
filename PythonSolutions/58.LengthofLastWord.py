class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s.split():
            return 0
        else:
            return len(s.split()[-1])
