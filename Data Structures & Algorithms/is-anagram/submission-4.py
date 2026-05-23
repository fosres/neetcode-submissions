class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        stable = [0] * 26

        ttable = [0] * 26

        i = 0

        while i < len(s):

            stable[ord(s[i]) - ord('a')] += 1

            i += 1

        j = 0

        while j < len(t):

            ttable[ord(t[j])-ord('a')] += 1

            j += 1

        k = 0

        return stable == ttable




        