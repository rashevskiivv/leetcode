class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time - O(n)
        # space - O(1)
        # ord('a') = 97
        # chr(97) = 'a'
        letters = {}
        for i in range(97, 97+26):
            letters[chr(i)] = 0
        for char in s:
            letters[char] += 1
        for char in t:
            letters[char] -= 1
        for _, count in letters.items():
            if count != 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))  # True
    print(Solution().isAnagram("ab", "a"))  # False
    print(Solution().isAnagram("rat", "car"))  # False
