class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for i in range(len(prefix)):
            for string in strs[1:]:
                if i >= len(string) or string[i] != prefix[i]:
                    return prefix[:i]

        return prefix