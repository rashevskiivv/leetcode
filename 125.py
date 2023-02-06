class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return ord('A') <= ord(c) <= ord('Z') or \
               ord('a') <= ord(c) <= ord('z') or \
               ord('0') <= ord(c) <= ord('9')

        # s = ''.join(filter(str.isalnum, s)).lower()
        # for i in range(len(s) // 2):
        #     if s[i] != s[len(s) - (i + 1)]:
        #         return False
        # return True

        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome("0P"))
    print(Solution().isPalindrome("mannam"))
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(Solution().isPalindrome("race a car"))  # False
