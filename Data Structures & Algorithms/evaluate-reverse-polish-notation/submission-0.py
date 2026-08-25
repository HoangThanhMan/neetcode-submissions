class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for tok in tokens:
            if self.is_operator(tok):
                num2 = st[-1]
                st.pop()
                num1 = st[-1]
                st.pop()
                st.append(self.compute(num1, num2, tok))
            else:
                st.append(int(tok))

        return st[-1]

    def is_operator(self, tok):
        return tok == '+' or tok == '-' or tok == '*' or tok == '/'

    def compute(self, num1, num2, tok):
        if tok == '+':
            return num1 + num2
        elif tok == '-':
            return num1 - num2
        elif tok == '*':
            return num1 * num2
        else:
            return int(num1 / num2)