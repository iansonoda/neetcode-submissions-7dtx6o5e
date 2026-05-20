class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""

        for string in strs:
            out += str(len(string)) + "#" + string

        return out       

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1 + length
            res.append(s[j + 1:i])

        return res