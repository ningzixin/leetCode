class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        cop = re.compile("[^a-z^A-Z^0-9]")  # 匹配不是中文、大小写、数字的其他字符
        s = cop.sub('', s)  # 将string1中匹配到的字符替换成空字符
        if s.upper() == s[::-1].upper():
            return True
        return False
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))