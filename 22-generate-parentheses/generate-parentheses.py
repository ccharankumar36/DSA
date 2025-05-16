class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s = []
        res = []
        def combination(open, close):
            if open == close == n:
                res.append(''.join(s))
                return
            if open < n:
                s.append('(')
                combination(open + 1, close)
                s.pop()
            if close < open:
                s.append(')')
                combination(open, close + 1)
                s.pop()
        combination(0, 0)
        return res 