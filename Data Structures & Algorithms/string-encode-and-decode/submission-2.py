class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:

            return ""


        string = ""

        i = 0

        while i < len(strs):

            length = len(strs[i])

            string += chr(length)

            string += strs[i]

            i += 1

        return string

    def decode(self, s: str) -> List[str]:

        if s == "":

            return []

        lst = []

        i = 0

        while i < len(s):

            length_str = s[i]

            length_int = ord(length_str)

            lst.append(s[i+1:i+1+length_int])

            i += ( length_int + 1)

        return lst


