class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}

        for char in s:
            seen1[char] = 1 + seen1.get(char, 0)

        for char in t:
            seen2[char] = 1 + seen2.get(char, 0)

        return seen1 == seen2