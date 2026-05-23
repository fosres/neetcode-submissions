class Solution:
    def isPalindrome(self, s: str) -> bool:

        t = ""

        i = 0

        while i < len(s):

            if s[i].isalnum():

                t += s[i].lower()

            i += 1

        print(t)

        i = 0

        j = len(t) - 1

        while i < j:

            if t[i] != t[j]:

                return False

            i += 1

            j -= 1
        
        return True