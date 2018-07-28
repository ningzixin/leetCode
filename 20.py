#python 栈

class s1:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        top = -1
        for i in s:
            if(top != -1 and s1.isMatching(self,stack[top],i)):
                stack.pop()
                top -= 1
                continue
            stack.append(i)
            top += 1
        if(top == -1):
            return True
        else:
            return False


    def isMatching(self,a,b):
        if(a == '('and b ==')'):
            return True
        if(a == '{'and b == '}'):
            return True
        if(a == '['and b == ']'):
            return True
        return False

print(s1.isValid('s',"([)]"))
