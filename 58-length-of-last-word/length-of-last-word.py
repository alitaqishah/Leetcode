class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1

        # Step 1: End ki spaces skip karo
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Step 2: Last word count karo
        count = 0

        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count