class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(closeN, openN):
            if closeN == openN == n:
                res.append("".join(stack))
                return
            
            if closeN < openN:
                stack.append(")")
                backtracking(closeN + 1, openN)
                stack.pop()
            if openN < n:
                stack.append("(")
                backtracking(closeN, openN + 1)
                stack.pop()

        backtracking(0, 0)

        return res