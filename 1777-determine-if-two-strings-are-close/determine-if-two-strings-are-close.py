class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # Step 1: Length check
        if len(word1) != len(word2):
            return False

        # Step 2: Check same characters
        if set(word1) != set(word2):
            return False

        # Step 3: Count character frequencies
        freq1 = {}
        freq2 = {}

        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1

        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1

        # Step 4: Compare sorted frequencies
        return sorted(freq1.values()) == sorted(freq2.values())